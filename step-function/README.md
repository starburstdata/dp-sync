# Sample Step Function Deployment

The Data Product Synchronization process can be deployed as an AWS Step Function. Subtasks (listing Data Products, 
creating/updating/deleting a Data Product, etc.) are implemented as individual AWS Lambda functions that are called 
by the Step Function. An example implementation is described here

## Setup

### Installation

The Step Function is defined in `dp-sync.json`. You will need to substitute your AWS region and account number into
the ARNs for the placeholders `__REGION__` and `__ACCOUNT_NUMBER__`.

Lambda Functions should be created with names matching each python file in this directory. If different names are 
chosen, the step function definition should be updated accordingly. Each lambda will require a
[Layer](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) containing the api client libraries and
functional code. To create the layer, 
1. Create a conda environment (optional)
2. pip install -r requirements
3. run `./zip-lambda-layer.sh`
4. Upload the zip file created in the parent directory of this repo

If not using conda for dependency management, remove the lines
```shell
CONDA_ENV='/opt/homebrew/anaconda3/envs/tiaa-dp-sync'
conda activate "${CONDA_ENV}"
```
from `./zip-lambda-layer.sh`.

The Lambda Functions have been tested with Python 3.12 and 3.13. 

### Configuration
Credentials and other configuration information are stored in AWS Secrets Manager under the name 
`data-product-sync-parameters`. You may use a different name - update `RetrieveInputParameters.py` appropriately if
you do. This secret should contain a dictionary with appropriate values for each field:
```json
{
  "galaxy-host":"https://<account>.galaxy.starburst.io",
  "galaxy-client-id":"clientid",
  "galaxy-client-secret":"secret",
  "galaxy-sql-username":"user@company.com/appropriaterole",
  "galaxy-sql-password":"password",
  "galaxy-sql-cluster-url":"https://<cluster to use for data product creation>.trino.galaxy.starburst.io",
  "data-product-catalog":"catalog",
  "default-cluster":"default cluster for data product",
  "sep-host":"sep.hostname.com",
  "sep-password":"password",
  "sep-username":"user",
  "tag":"<this tag will be applied to all data products created through this process>",
  "search_string":"<only data products with names containing this string will be synced>"
}
```
Note that there are two sets of credentials for Galaxy. Galaxy requires using 
[authentication tokens](https://docs.starburst.io/starburst-galaxy/developer-tools/api/api-auth-token.html) for 
accessing the API, and a username/password pair for SQL clients. This process uses both interfaces.

This Secret will be accessed by the `RetrieveInputParameters` Lambda. When creating the Lambda, create an IAM policy
for accessing this Secret and apply it to the Lambda.

The timestamp of the last run is stored in a separate secret. This allows the process to segregate Data Products 
created since the last run, which will need to be newly created, from those that only need to be updated and refreshed.
This secret is named `dp-sync/data-product-sync-last-run-timestamp` by default, if a different name is chosen then 
update the `GetDataProducts` Lambda accordingly. Ensure that `GetDataProducts` has proper permissions to read the 
secret. It can be left empty or initialized to an arbitrary value. 
