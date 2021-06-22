import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    leaderboard_table = dynamodb.Table('leaderboard')
    
    user_name = event['user_name']
    has_item = False
    
    try:
        response = leaderboard_table.get_item(
            Key={
                'user_name': user_name
            }    
        )
        
        try:
            if response['Item'] is not None:
                has_item = True
        except:
            pass
        
        return {
            'statusCode': 200,
            'body': has_item
        }
    except Exception as e:
        print('Error. Closing lambda function.')
        return {
            'statusCode': 400,
            'body': json.dumps('Error checking for user. {}'.format(e))
        }