# Databricks Runtime 5.x has Python 3.5, Databricks Runtime 5.x ML has Python 3.6, and Databricks Runtime 6.x and Databricks Runtime 6.x ML have Python 3.7.
# awk this with a mapping
databricks cluster get --cluster-id $ID_CLUSTER_SPARK | grep spark_version