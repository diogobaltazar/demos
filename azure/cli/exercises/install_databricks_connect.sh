conda create --name $DATABRICKS_CONNECT_PYTHON_ENV python=$PYTHON_RUNTIME_CLUSTER_SPARK
pip uninstall pyspark
sudo pip install -U databricks-connect==$RUNTIME_CLUSTER_SPARK
databricks-connect configure
# Set new config values (leave input empty to accept default):
# Databricks Host [no current value, must start with https://]: $HOST_DATABRICKS
# Databricks Token [no current value]: $USER_TOKEN_DATABRICKS

# IMPORTANT: please ensure that your cluster has:
# - Databricks Runtime version of DBR 5.1+
# - Python version same as your local Python (i.e., 2.7 or 3.5)
# - the Spark conf `spark.databricks.service.server.enabled true` set

# Cluster ID (e.g., 0921-001415-jelly628) [no current value]: $ID_CLUSTER_SPARK
# Org ID (Azure-only, see ?o=orgId in URL) [0]: $ID_ORGANIZATION
# Port [15001]: $SERVICE_PORT_DATABRICKS

# Updated configuration in /home/diogo/.databricks-connect
# * Spark jar dir: /usr/local/lib/python2.7/dist-packages/pyspark/jars
# * Spark home: /usr/local/lib/python2.7/dist-packages/pyspark
# * Run `pip install -U databricks-connect` to install updates
# * Run `pyspark` to launch a Python shell
# * Run `spark-shell` to launch a Scala shell
# * Run `databricks-connect test` to test connectivity
databricks-connect test