from fastapi import FastAPI
import boto3
from pydantic import BaseModel
import os

app = FastAPI()

# Get AWS credentials from environment variables
aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
region_name = os.getenv('AWS_DEFAULT_REGION', 'us-east-1')

# DynamoDB client
dynamodb = boto3.resource(
    'dynamodb',
    region_name=region_name,
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Define a Pydantic model for the items
class Item(BaseModel):
    id: str
    name: str

@app.get("/")
def read_root():
    return {"FastAPI & DynamoDB": "Microservice"}

@app.post("/items")
def create_item(item: Item):
    table = dynamodb.Table('Items')  
    table.put_item(Item=item.dict())
    return item

@app.get("/items")
def read_items():
    table = dynamodb.Table('Items')
    response = table.scan()
    items = response.get('Items', [])
    if items:
        return items
    return {"error": "No items found"}
