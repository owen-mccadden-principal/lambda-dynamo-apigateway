import json
import boto3

def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')
    leaderboard_table = dynamodb.Table('leaderboard')
    
    user_name = event['user_name']
    score = event['score']
    
    try:
        leaderboard_table.update_item(
            Key={
                'user_name': user_name,
            },
            UpdateExpression="SET score = :val",
            ExpressionAttributeValues={
            ':val': int(score)
            },
            ReturnValues="UPDATED_NEW"
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps('Successfully updated score')
        }
    except Exception as e:
        print('Error. Closing lambda function.')
        return {
            'statusCode': 400,
            'body': json.dumps('Error updating the score. {}'.format(e))
        }