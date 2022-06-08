from uuid import uuid4

from boto3.dynamodb.conditions import Key


DEFAULT_USERNAME = 'default'


class OrderDB(object):
    def list_items(self):
        pass

    def add_item(self,phone,agency,name ,description,company,deadline, category=None):
        pass

    def get_item(self, uid):
        pass

    def delete_item(self, uid):
        pass

    def update_item(self, uid,phone=None,agency=None,name=None ,description=None,company=None,deadline=None, category=None):
        pass

class DynamoDBOrder(OrderDB):
    def __init__(self, table_resource):
        self._table = table_resource

    def list_all_items(self):
        response = self._table.scan()
        return response['Items']

    def list_items(self, username=DEFAULT_USERNAME):
        response = self._table.query(
            KeyConditionExpression=Key('username').eq(username)
        )
        return response['Items']

    def add_item(self, name,phone,agency,company,description, deadline,category=None, username=DEFAULT_USERNAME):
        uid = str(uuid4())
        self._table.put_item(
            Item={
                'username': username,
                'name': name,
                'phone': phone,
                'agency': company,
                'company': company,
                'deadline': deadline,
                'uid': uid,
                'description': description,
                'state': 'unstarted',
                'category': category if category is not None else {},
            }
        )
        return uid

    def get_item(self, uid, username=DEFAULT_USERNAME):
        response = self._table.get_item(
            Key={
                'username': username,
                'uid': uid,
            },
        )
        return response['Item']

    def delete_item(self, uid, username=DEFAULT_USERNAME):
        self._table.delete_item(
            Key={
                'username': username,
                'uid': uid,
            }
        )

    def update_item(self, uid, state=None,phone=None,agency=None,name=None ,description=None,company=None,deadline=None, category=None, username=DEFAULT_USERNAME):


                    
        # We could also use update_item() with an UpdateExpression.
        item = self.get_item(uid, username)
        if name is not None:
           item['name'] = name
        if phone is not None:
            item['phone'] = phone
        if agency is not None:
            item['agency'] = agency
        if company is not None:
                item['company'] = company
        if description is not None:
            item['description'] = description
        if state is not None:
            item['state'] = state
        if category is not None:
            item['category'] = category
        if deadline is not None:
            item['deadline'] = deadline
        self._table.put_item(Item=item)
