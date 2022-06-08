import os
import base64

import boto3
from chalice import Chalice, AuthResponse
from chalicelib import auth, db


app = Chalice(app_name='refera')
app.debug = True
_DB = None
USERNAME="Admin"
_USER_DB = None
_AUTH_KEY = None
_SSM_AUTH_KEY_NAME = '/order/auth-key'

@app.route('/login', methods=['POST'])
def login():
    body = app.current_request.json_body
    record = get_users_db().get_item(
        Key={'username': body['username']})['Item']
    jwt_token = auth.get_jwt_token(
        body['username'], body['password'], record, get_auth_key())
    return {'token': jwt_token}


@app.authorizer()
def jwt_auth(auth_request):
    token = auth_request.token
    decoded = auth.decode_jwt_token(token, get_auth_key())
    return AuthResponse(routes=['*'], principal_id=decoded['sub'])


def get_auth_key():
    global _AUTH_KEY
    if _AUTH_KEY is None:
        base64_key = boto3.client('ssm').get_parameter(
            Name=_SSM_AUTH_KEY_NAME,
            WithDecryption=True
        )['Parameter']['Value']
        _AUTH_KEY = base64.b64decode(base64_key)
    return _AUTH_KEY


def get_users_db():
    global _USER_DB
    if _USER_DB is None:
        _USER_DB = boto3.resource('dynamodb').Table(
            os.environ['USERS_TABLE_NAME'])
    return _USER_DB


def get_app_db():
    global _DB
    if _DB is None:
        _DB = db.DynamoDBOrder(
            boto3.resource('dynamodb').Table(
                os.environ['APP_TABLE_NAME'])
        )
    return _DB


def get_authorized_username(current_request):
    return current_request.context['authorizer']['principalId']


@app.route('/orders', methods=['GET'])
def list_orders():

    return get_app_db().list_items()


@app.route('/orders', methods=['POST'])
def create_order():
    body = app.current_request.json_body
    return get_app_db().add_item(
        
         name=body['name'],
        phone=body['phone'],
        agency=body['agency'],
        description=body['description'],
        company=body['company'],
        deadline=body['deadline'],
        category=body.get('category'),
        
    )


@app.route('/orders/{uid}', methods=['GET'])
def get_order(uid):
    return get_app_db().get_item(uid)


@app.route('/orders/{uid}', methods=['PUT'])
def update_order(uid):
    body = app.current_request.json_body
    get_app_db().update_item(
        uid,
         name=body['name'],
        contact=body['phone'],
        agency=body['agency'],
        description=body['description'],
        company=body['company'],
        deadline=body['deadline'],
        category=body.get('category'),)


@app.route('/orders/{uid}', methods=['DELETE'])
def delete_order(uid):
    return get_app_db().delete_item(uid)

@app.route('/categories', methods=['GET'])
def list_orders():
    return get_app_db().list_items()




@app.route('/categories', methods=['POST'])
def create_order():
    body = app.current_request.json_body
    return get_app_db().add_item(
         name=body['name'],
        phone=body['phone'],
        agency=body['agency'],
        description=body['description'],
        company=body['company'],
        deadline=body['deadline'],
        category=body.get('category'),
        
    )


@app.route('/categories/{uid}', methods=['GET'])
def get_order(uid):
    return get_app_db().get_item(uid)


@app.route('/categories/{uid}', methods=['PUT'])
def update_order(uid):
    body = app.current_request.json_body
    get_app_db().update_item(
        uid,
         name=body['name'],
        contact=body['phone'],
        agency=body['agency'],
        description=body['description'],
        company=body['company'],
        deadline=body['deadline'],
        category=body.get('category'),)


@app.route('/categories/{uid}', methods=['DELETE'])
def delete_order(uid):
    return get_app_db().delete_item(uid)
