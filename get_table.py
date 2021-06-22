import json
import boto3
import math

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    leaderboard_table = dynamodb.Table('leaderboard')
    
    try:
        response = leaderboard_table.scan()
        sorted_items = sorted(response['Items'], key=lambda x: x['score'], reverse=True)
        return {
            'statusCode': 200,
            'body': sorted_items
        }
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps('Error getting table. {}'.format(e))
        }
    
    
