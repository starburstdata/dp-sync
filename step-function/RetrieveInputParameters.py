import boto3
import json


def lambda_handler(event, context):
    # Initialize Secrets Manager client
    secrets_manager = boto3.client('secretsmanager')

    # Retrieve secret
    secret_name = "data-product-sync-parameters"
    response = secrets_manager.get_secret_value(SecretId=secret_name)
    secret = json.loads(response['SecretString'])

    # Add retrieved parameters to the event for the next step
    event.update({
        'sep_host': secret['sep_host'],
        'sep_username': secret['sep_username'],
        'sep_password': secret['sep_password'],
        'galaxy_host': secret['galaxy_host'],
        'galaxy_client_id': secret['galaxy_client_id'],
        'galaxy_client_secret': secret['galaxy_client_secret'],
        'galaxy_sql_username': secret['galaxy_sql_username'],
        'galaxy_sql_password': secret['galaxy_sql_password'],
        'galaxy_sql_cluster_url': secret['galaxy_sql_cluster_url'],
        'data_product_catalog': secret['data_product_catalog'],
        'default_cluster': secret['default_cluster']
    })

    # Pass updated event to next Lambda
    return event
