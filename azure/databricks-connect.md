**install databricks-connect windows** [here](https://datathirst.net/blog/2019/4/20/setup-databricks-connect-on-windows)

Check whether the java version is the version 8:
```bash
> java -version
java version "1.8.0_181"
Java(TM) SE Runtime Environment (build 1.8.0_181-b13)
Java HotSpot(TM) 64-Bit Server VM (build 25.181-b13, mixed mode)
```

Move the java installation dir out of `Program Files` in order not to have a name with spaces.

**sync visual studio to databricks**
[here](https://datathirst.net/blog/2019/3/7/databricks-connect-finally)

Developing sw on the azure databricks browser ui can be quite disturbing. The ado repository should be cloned and developed locally, and executed in the cloud, in the databricks spark cluster.

get remote solution  
TODO  

visual studio profile
+ choose profile with access rights to the azure devops code repository  

source code
+ under `Team Explorer`, click on `Manage Connections`, select an organization `<org.ado>`, then the project `<proj.org.ado>`and finally the repository `<repo.proj.org.ado>`.  

version control  
+ Use the `Team Explorer` to perform version control operations.  

develop
+ install `databricks-connect`
+ verify that the cluster's databricks runtime version is 5.1 or higher
+ edit the spark config file:

```json
{
    "autoscale": {
        "min_workers": 2,
        "max_workers": 13
    },
    "cluster_name": "<az-cluster-name>",
    "spark_version": "5.5.x-scala2.11",
    "spark_conf": {
        "spark.databricks.service.server.enabled": "true",
        "spark.databricks.service.port": "8787",
        "spark.executor.cores": "4",
        "spark.executor.memory": "20G",
        "spark.executor.instances": "4",
        "spark.databricks.delta.preview.enabled": "true",
        "spark.sql.orc.enableVectorizedReader": "false",
        "spark.sql.parquet.int96AsTimestamp": "true"
    },
    "node_type_id": "Standard_E16s_v3",
    "driver_node_type_id": "Standard_E16s_v3",
    "ssh_public_keys": [],
    "custom_tags": {},
    "spark_env_vars": {
        "PYSPARK_PYTHON": "/databricks/python3/bin/python3"
    },
    "autotermination_minutes": 30,
    "enable_elastic_disk": true,
    "cluster_source": "UI",
    "init_scripts": [],
    "cluster_id": "<az-cluster-id>"
}
```

+ create a new conda environment: `$ conda create --name <local-python-environment> python=<python-version.spark-cluster>`
+ install a vs terminal, *e.g.*: (whack whack terminal)[https://marketplace.visualstudio.com/items?itemName=dos-cafe.WhackWhackTerminal]. Open the terminal with `Ctrl + \ + Ctrl + \`
+ open terminal and execute `$ databricks-connect configure` editing the values as:
    + `<az-databricks-host>`
    + `<az-databricks-usr-token>`
    + `<az-cluster-id>`
    + `<organization-id>`
    + `<cluster-port>`/*
/* this is why the port was explicitly defined in the cluster config
+ Output:
```bash
IMPORTANT: please ensure that your cluster has:
- Databricks Runtime version of DBR 5.1+
- Python version same as your local Python (i.e., 2.7 or 3.5)
- the Spark conf `spark.databricks.service.server.enabled true` set
[...]
Updated configuration in C:\Users\Utilizador/.databricks-connect
* Spark jar dir: c:\users\utilizador\anaconda3\lib\site-packages\pyspark/jars
* Spark home: c:\users\utilizador\anaconda3\lib\site-packages\pyspark
* Run `pip install -U databricks-connect` to install updates
* Run `pyspark` to launch a Python shell
* Run `spark-shell` to launch a Scala shell
* Run `databricks-connect test` to test connectivity
```
+ run `databricks-connect test` to test the connetivity and fix all errors
+ execute: `F5`

CONTINUE....


-----

[here](https://datathirst.net/blog/2019/4/20/setup-databricks-connect-on-windows)

