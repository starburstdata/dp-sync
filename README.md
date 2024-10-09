# Data Product Sync Tool

Synchronize the Data Products from a SEP cluster to a Galaxy account. This will
* Create a new Galaxy data product for any SEP Data Product that does not exist in Galaxy
* Update any existing data products
* Refresh the View definitions for all logical view datasets
* Point Materialized View datasets at the latest available storage table

Note that because SEP Data Products only support Hive Materialized Views, and Galaxy cannot read 
Hive Materialized Views, the sync process creates a logical view pointing at the storage table. This
avoids any data duplication, but may lead to Galaxy reading from a stale view until the next run 
of the sync process.

## Requirements

* All catalogs referenced by Logical View datasets must be present in Galaxy with the same name. No view rewriting is performed
* Galaxy must have permission to read the Hive Materialized View Storage Tables. If the Glue catalog is used, 
then this may require setting up access for your Galaxy cross-account role in LakeFormation. If the HMS is used, ensure Galaxy
can connect to it
* Dataset descriptions, including column descriptions, are not suppoerted in Galaxy and will not be copied
* Data Product owners and contacts must be registered users in the Galaxy account, and must use the same email for registration 
as they used for the Data Product

## Run Locally

You can `python runner.py <args>` from your local environment. 

## Run in AWS Step Function
TODO
