import boto3
import json


def lambda_handler(event, context):
    secrets_manager = boto3.client('secretsmanager')

    # Update run timestamp
    secret_name = "data-product-sync-timestamp"
    search_time = event['search_time']

    secrets_manager.put_secret_value(
        SecretId=secret_name,
        SecretString=json.dumps(search_time)
    )

    return event
