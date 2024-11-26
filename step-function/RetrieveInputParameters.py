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
        'sep_host': secret['sep-host'],
        'sep_username': secret['sep-username'],
        'sep_password': secret['sep-password'],
        'galaxy_host': secret['galaxy-host'],
        'galaxy_client_id': secret['galaxy-client-id'],
        'galaxy_client_secret': secret['galaxy-client-secret'],
        'galaxy_sql_username': secret['galaxy-sql-username'],
        'galaxy_sql_password': secret['galaxy-sql-password'],
        'galaxy_sql_cluster_url': secret['galaxy-sql-cluster-url'],
        'data_product_catalog': secret['data-product-catalog'],
        'default_cluster': secret['default-cluster'],
        'search_string': secret.get('search_string'),
        'tag': secret.get('tag')
    })

    # Pass updated event to next Lambda
    return event
