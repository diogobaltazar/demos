# databricks
## workspace
Create new `databricks` service with:
+ name `name=demo-workspace`
+ resource group `resource-group=demo-resource-group`
+ region `region=West Europe` or `region=westeurope`
+ pricing tier `pricing-tier=Standard (Apache Spark, Secure with Azure AD)`
+ not deploying azure databricks workspace on my own virtual network
+ with id `workspace-id=https://<region>.azuredatabricks.net/?o=<workspace_id>`
+ where `<workspace-id>=5053541570930551`

Notice that the creation of the service under `demo-resource-group` has created
+  a workspace
+ three resources in the same group, the *data plane resources*:
    + virtual network deployed in the data plane, `workers-vnet`;
    + network security group to manage the inbound and outbound traffic, `workers-sg`;
    + underlying storage account for DBFS, `dbstoragen6iazla6qslaq`;

The service has available:
+ workspace: assets
+ data, manage the databases
+ clusters, crt and manage the clusters
+ jobs, deploy the jobs

Create project ``workspace/demo-proj`` on the workspace.


## spark cluster pool of instances
Create spark cluster pool:
+ `<cluster-pool>=demo-interactive-spark-cluster-pool`
+ `<cluster-min-idle>=1`
+ `<cluster-max-capacity>=3`
+ `<instance-type>=Standard_DS3_v2`

Note that the pool will display a minimal number of instances of 1 as defined.

json config
```json
{
    "autoscale": {
        "min_workers": 1,
        "max_workers": 2
    },
    "cluster_name": "demo-interactive-spark-cluster",
    "spark_version": "5.5.x-scala2.11",
    "spark_conf": {},
    "ssh_public_keys": [],
    "custom_tags": {},
    "spark_env_vars": {
        "PYSPARK_PYTHON": "/databricks/python3/bin/python3"
    },
    "autotermination_minutes": 120,
    "cluster_source": "UI",
    "init_scripts": [],
    "instance_pool_id": "1026-201213-moody208-pool-5brMO7nU",
    "cluster_id": "1026-221605-dizzy655"
}
```

## spark cluster

To be able to create a spark cluster, the subscription should be upgraded from `Free Trial` to `Pay-As-You-Go`, otherwise it will not be possible to create more than one worker node:
+ `<subscription-name>=demo_pay_as_you_go_subscription`
+ `<subscription-support-plan>=No technical support or I'm already covered through Microsoft Premier Support.`

Without considering the pool, creating a spark cluster:
+ `<cluster-name>=clusters/demo-interactive-spark-cluster`
+ `<cluster-mode>=Standard`
+ `<pool>=None`
+ `<Databricks Runtime Version>=6.1 (Scala 2.11, Spark 2.4.4)`
+ with `<autoscaling-enabled>` and `<min-workers>=1`, `<max-workers>=3`
+ and `<cluster-terminate>=60mns of inactivity`
+ ``<worker-node-config>=Standard_DS3_v2``
+ ``<driver-node-config>=Standard_DS3_v2``
+ ``<azure-data-lake-storage-credential-passthrough>=not defined``
+ ``<spark-config>=not defined``
+ ``<environment-variables>=not defined``

Mind the `Event Log` and the `Driver Logs`

Regarding the pool, creating the spark cluster no longer allows us to define the **nodes instance types**:
+ `<pool>=demo-interactive-spark-cluster-pool`

# active directory single sign-on

-----
# exercises
1. create a cluster associated to a pool of instances and cluster without being associated to a pool of instances, and compare the execution time of launching instances.


-----
[subscription-plan](https://docs.microsoft.com/en-us/azure/azure-databricks/quickstart-create-databricks-workspace-portal#targetText=To%20use%20a%20free%20account,and%20then%20click%20Launch%20Workspace.)