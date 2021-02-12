import json
import boto3

# code for DynamoDB timing
table_name = 'gsa-lambda-timing-table'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

# subtract timestamps to calculate DB delays
import time
def lambda_handler(event, context):
    print("#1")
    print("Time before writing to DB: ", time.time())
    response = table.put_item(
        Item = {
            'key': event['key'],
            'value': event['value']
        }
    )
    print("Time after writing to DB: ", time.time())
    
    print("#2")
    print("Time before writing to DB: ", time.time())
    response = table.put_item(
        Item = {
            'key': event['key'],
            'value': event['value']
        }
    )
    print("Time after writing to DB: ", time.time())
    
    print("#3")
    print("Time before writing to DB: ", time.time())
    response = table.put_item(
        Item = {
            'key': event['key'],
            'value': event['value']
        }
    )
    print("Time after writing to DB: ", time.time())
    
    print("#4")
    print("Time before writing to DB: ", time.time())
    response = table.put_item(
        Item = {
            'key': event['key'],
            'value': event['value']
        }
    )
    print("Time after writing to DB: ", time.time())
    
    print("#5")
    print("Time before writing to DB: ", time.time())
    response = table.put_item(
        Item = {
            'key': event['key'],
            'value': event['value']
        }
    )
    print("Time after writing to DB: ", time.time())
    
    return response
