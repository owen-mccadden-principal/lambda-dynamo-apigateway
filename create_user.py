import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    leaderboard_table = dynamodb.Table('leaderboard')
    
    user_name = event['user_name']
    score = 0
    
    try:
        leaderboard_table.put_item(
            Item={
                'user_name': user_name,
                'score': int(score)
            }    
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Successfully created user.')
        }
    except Exception as e:
        print('Error. Closing lambda function.')
        return {
            'statusCode': 400,
            'body': json.dumps('Error creating the user. {}'.format(e))
        }
