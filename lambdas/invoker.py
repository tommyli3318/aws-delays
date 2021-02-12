import json
import urllib3
from time import sleep
import os

http = urllib3.PoolManager()

def lambda_handler(event, context):
    api_endpoint = os.environ['API_ENDPOINT']
    
    http.request('POST', api_endpoint, fields={'key': 'k', 'value': 1})
    sleep(1)
    
    http.request('POST', api_endpoint, fields={'key': 'k', 'value': 1})
    sleep(1)
    
    http.request('POST', api_endpoint, fields={'key': 'k', 'value': 1})
    sleep(1)
    
    http.request('POST', api_endpoint, fields={'key': 'k', 'value': 1})
    sleep(1)
    
    http.request('POST', api_endpoint, fields={'key': 'k', 'value': 1})
    sleep(1)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Invoked other lambda 5 times (1 second delay between each invocation)')
    }
