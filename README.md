# refera-fullstack-challenge-
Technical Specification
Refera - Fullstack Code Challenge

Introduction
This is a web application to manage maintanence orders from Refera.This app makes ause of  a serverless web API to create, update, get, and delete Orders, managing Orders in a database, and adding authorization with JWT. AWS services covered include AWS Lambda, Amazon API Gateway, Amazon DynamoDB, AWS CodeBuild, and React .

Architecture
The main component of this application is a REST API backed by Amazon API Gateway and AWS Lambda. In order to see a list of Order items, must first log in. Information about  users is stored in an Amazon DynamoDB table. The authentication is done using a builtin authorizer (JSON Web Tokens ). This lets you define a Lambda function to perform your custom auth process. 


Architecture Diagram 

https://refera-challenge.s3.eu-west-2.amazonaws.com/diagram.JPG

REST API
The REST API supports the following resources:
Order API:
GET - /orders/ - Gets a list of all  orders
POST - /orders/ - Creates a new  order
GET - /orders/{id} - Gets a specific order
DELETE - /orders/{id} - Deletes a specific order
PUT - /orders/{id} - Updates the state of a order

Category API:
GET - /categories/ - Gets a list of all  categories
POST - /categories/ - Creates a new  category
GET - /categories/{id} - Gets a specific category
DELETE - /categories/{id} - Deletes a specific category
PUT - /categories/{id} - Updates the state of a category
Development mode
 Create an env and install all the dependencies  on the under requirements.txt on the project the run chalice local and  make requests to http://localhost:8000/.
Production environment
Rest API URL: https://28pr9svp46.execute-api.us-east-1.amazonaws.com/api/
App  URL : http://refera-challenge.s3-website.eu-west-2.amazonaws.com/
