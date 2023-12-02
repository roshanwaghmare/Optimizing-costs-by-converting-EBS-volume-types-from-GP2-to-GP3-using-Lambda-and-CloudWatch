import json
import boto3

def get_volume_id_from_arn(volume_arn):
    #split the ARN using colon (':') separator
    arn_parts = volume_arn.split(':')
    # The volume id is the last part of the ARN after the 'volume/' prefix
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id
    
    
def lambda_handler(event, context):
    
    event = {
       "version":"0",
       "id":"0c449b5a-ea88-53b7-7d40-133a4575e53b",
       "detail-type":"EBS Volume Notification",
       "source":"aws.ec2",
       "account":"688646276098",
       "time":"2023-12-02T09:17:34Z",
       "region":"ap-south-1",
       "resources":[
          "arn:aws:ec2:ap-south-1:688646276098:volume/vol-0dc832820fb7fdcc0"
       ],
       "detail":{
          "result":"available",
          "cause":"",
          "event":"createVolume",
          "request-id":"4be3ed0f-58d3-408d-9489-42ac627ec0a2"
        }
    } 

    volume_arn = event[resources][0]
    volume_id = get_volume_id_from_arn(volume_arn)
    
    ec2_client = boto3.client('ec2')
    
    response = client.modify_volume(
    VolumeId=volume_id,
    VolumeType='gp3',
)
    
    print(event)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }




# NEW CODE

import boto3

def get_volume_id_from_arn(volume_arn):
    # Split the ARN using colon (':') separator
    arn_parts = volume_arn.split(':')
    # The volume id is the last part of the ARN after the 'volume/' prefix
    volume_id = arn_parts[-1].split('/')[-1]
    return volume_id

def lambda_handler(event, context):
    # Use correct syntax for accessing 'resources' in the event dictionary
    volume_arn = event['resources'][0]
    volume_id = get_volume_id_from_arn(volume_arn)
    
    # Use correct variable name 'ec2_client'
    ec2_client = boto3.client('ec2')
    
    # Use the correct variable name 'ec2_client' in the following line
    response = ec2_client.modify_volume(
        VolumeId=volume_id,
        VolumeType='gp3',
    )
   

