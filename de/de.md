coupling  
    density of dependencies between components  
cohesion  
scalability  
throughput  
latency  
redundancy  
availability  
lazy-evaluation  
resiliency  
transactions  
mutability  
stream-data
batch-data
LDAP
+ lightweight-directory-access-protocol
+ authentication protocol
AD
+ active-directory
+ uses the LDAP protocol
lineage-graph.computation.dataset 
+ enables:
+ data lineage
+ fault-recovery by recalculating through the lineage graph should data be missing/corrupted
 application-performance-management
+ monitor application resource consumption
data-lineage  
fault-tolerant  
elastic-search  
relational-database  
+ big data information systems no longer required **normzalization rules** due to ease on processing big data quantities
solr 
scalability.cloud.distributed.system 
+ scale up/down bandwidth demands
disaster-recovery.cloud.distributed.system
+ avoids large up-front investment and third-party expertise
+ avoids maintenince
+ data distributed accross different servers in different data centers in different regions 
sys-updates-and-maintenaince.cloud.distributed.system
+ no system update maintenaince
+ no security maintenaince
capital-expenditure-free.cloud.distributed.system
+ no infrastructure maintenaince
+ no expensive access devices needed (laptops)
+ pay-as-you-go
+ scale carbon footprint
incremental
snapshot
increased-collaboration.cloud.distributed.system
+ cloud-based workflow enables more visibility and cooperation
+ device agnostic (single requirement: connectivity and a browser)
+ geography agnostic
+ time-zone agnostic
security.cloud.distributed.system
+ no sensitive data lost with stolen laptops
+ regions for data privacy (compliance)
scalability.attributes.computing.cloud  
    meet demand  
    vertically: launch/close applications on-demand  
    horizontally: add/close resources to the applications on-demand  
elasticity.attributes.computing.cloud  
pooling.attributes.computing.cloud  
+ terminating a cluster when not in use and booting it again is costly (time)
+ create a pool with ready-to-use *instances*
+ the pool is attached to multiple clusters that request instances
+ the pool creates more instances if required, and terminates them if nobody needs them, always keeping available a couple of instances
+ pros: increases start and auto-scalling time
provisioning.attributes.computing.cloud  
cloud.azure.delivery.models  
cloud.azure.infrastructure.models.SaaS  
    for customers  
    office 365 in OneDrive  
cloud.azure.infrastructure.models.PaaS  
    for developpers  
compute.PaaS.models.infrastructure.azure.cloud
    + web-apps
    + API-aps
    + serverless functions
    + database
IaaS.models.infrastructure.azure.cloud
compute.IaaS.models.infrastructure.azure.cloud
+ VMs
spark
+ framework to transform and perform analytics on data
pool.spark-cluster.distributed.system
+ pool of instances/vms for multiple spark clusters
+ properties:
    + idle instance auto termination: define whether to terminate an instance/vm after a number of minutes
    + minimum idle instances: number of instances/vms always running in the pool
    + maximum capacity: upper limit of instances/vms in the pool. If clusters demand more instances/vms than those available, and more than those defined in the max capacity, it will result in a failure.
    + instance type: if a cluster is attached to a pool, the driver and the worker vm nodes have to use the instance config specified in the pool
spark-cluster.distributed.system
+ the spark distributed system running the spark engine
spark-core.distributed.system
+ distributed computing engine
rdd.distributed.system
+ does not impose structure on data (++freedom, --performance, ++complexity)
+ resilient distributed dataset
+ in-memory object
+ redundancy across cluster nodes
+ parallel computing across cluster nodes
+ lazy transformations
+ immutable/read-only: each transformation creates a new RDD
+ lineage graph: the set of transformations over a dataset
+ the lineage graph enables:
    + data lineage
    + fault-recovery by recalculating through the lineage graph should data be missing/corrupted/node crash
table.distributed.system
dataframe.distributed.system
+ tabular schema API on top of RDD
+ domain specific language API for manipulations
+ with tabular schema: ++performance
+ untyped: collection of Row objects, untyped JVM objects
dataset.distributed.system
+ tabular schema API on top of RDD
+ domain specific language API for manipulations
+ with tabular schema: ++performance
+ typed: collection of typed-Row objects, typed JVM objects, where the types are declared in a Java/Scala class
+ datasets are not available for PySpark/RSpark because they have **no compile-time type-safety**
sparksql.spark.distributed.system
    + structured data processing: pyspark, etc.
compile-time-type-safety
graphx.spark.distributed.system
    + graph data processing
storage.IaaS.models.infrastructure.azure.cloud
networking.IaaS.models.infrastructure.azure.cloud
aks.azure.cloud  
    azure container/kubernettes service  
regions.azure.cloud  
    data and compute centers connected whithin a latency perimeter  
    choosing:  
    + latency - the regions for the services provided should be close to the customers of the services for better servicing  
    + cost - varies per region, Bay Area more expensive than Ohio with all the tech companies fighting for the same real estate  
    + country compliance laws, either of the company's, or of the client's. It may be of interest to put the data on a region where the gov cannot go fetch the data.  
    + data/compute center's features  
    + disaster recovery - redundancy accross regions is better than in a single region. Tsunami.  
geography.azure.cloud  
    {regions} for compliance and data residency purposes  
dev-test-labs.azure
dbfs.file-system.databricks.azure.cloud
+ distributed file sytem mounted into an azure databricks workspace and accessible from azure databricks clusters.
+ abstraction on top of scalable objects store
single-sign-on.databricks. azure.cloud
+ persists data in azure-storage
azure-storage.data-persistence.azure.cloud
databricks.azure.cloud
+ unified analytics platform optimized for the cloud
+ architecture:
    1. workspace: 
    1. runtime: exec-environments
    1. cloud service: spark-cluster (over azure or aws) 
+ crt and manage optimized auto-scaling spark-cluster environments:
    + standard
    + serverless
+ workspace for collaboration
+ dataset build automation
+ brings together data engineering and data science workloads
+ clusters need to be terminated explicitly
runtime-version.databricks.azure.cloud
+ vm image with  pre-installed libraries with a specific version of spark, python|scale|... and other libraries
+ each runtime has a version:
    + ML
    + acceletared GPU
event-log.spark-cluster.databricks.azure.cloud  
+ logs about the cluster: ``CREATING``, ``TERMINATING``, *etc.*
driver-logs.spark-cluster.databricks.azure.cloud  
+ logs of jobs being executed in the cluster
dbu.databricks-unit.databricks.azure.cloud  
+ capacity of processing per hour
+ 0.75 DBUs means the running of a vm during one hour will consume 0.75 DBUs
+ Azure charges by **DBU**
worker-node.interactive-spark-cluster.spark-cluster.databricks.azure.cloud  
+ the runtime vm definition will apply to all worker nodes
driver-node.interactive-spark-cluster.spark-cluster.databricks.azure.cloud  
+ also known as **master node**
job-spark-cluster.spark-cluster.databricks.azure.cloud 
+ also known as automated-spark-cluster.spark-cluster.databricks.azure.cloud 
+ used to run automated jobs, which require cluster config while setting up a job
+ the cluster is created when the job starts, terminating when the job ends
+ the cluster cannot be created by a user
+ auto-scale on demand
+ cons: all the resources get locked/dedicated to the job
interactive-spark-cluster.spark-cluster.databricks.azure.cloud  
+ cluster used to interact with the data through `notebooks`
+ created by users or by `crt cluster api`. Remember they do not auto terminate. I'll be charged whenever they are running, even of they're not being used.  Databricks enables the user to terminate the clusters if they're inactive for a given period of time.
+ auto-scale on demand
+ cons: need to be explicitly shut down
+ modes:
    + standard-mode: meant for single users, single users using the same cluster, and it does not provide **fault isolation**, if multiple users are working on the same cluster, failing in the code execution of one user may affect other users; It also does not guarantee **task preemption**, so one user can consume all the resources and block them for other users. It is thus recommended (for specific UC) that each user works in his own separate cluster. Standard clusters support multiple languages.
    + high-concurrency-mode: supports mulitple users, with **fault isolation** and **task preemption**. This guarantees maximum usage of the cluster, saving costs. cons: python, sql, r, not scala; 
standard-spark-cluster.spark-cluster.databricks.azure.cloud  
+ different users share single cluster and it's resources
databricks-serverless.spark-cluster.databricks.azure.cloud
+ a spark-cluster designed for high concurrency
+ each user accesses a shared pool of resources, granting isolation for the user spark environment
idempotent
optimize.databricks.azure.cloud
+ Optimize the layout of data stored in DBFS. Optionally optimize a subset of data or colocate data by column.
datalake
+ framework to ingest different sources/types of data
    + batch/stream data
    + ...
+ the data is stored in a **common storage repository**
    + divided in layers:
        + raw
        + cleansed
        + features/transformed
        + pub
+ data governance
    + data access policies
    + data lineage
+ application layer
    + dashboards
    + analytics
delta-lake.databricks.azure.cloud
+ a data lake is difficult to manage
+ open-source storage layer that adds features/structure to data lake files:
    + ACID operations over the same file
    + schema enforcement
    + full dml support
    + rollback
database.databricks.azure.cloud
+ collection of tables
table.databricks.azure.cloud
+ collection of structured data
+ equivalent to dataframes
metastore.databricks.azure.cloud
+ [metastore](https://docs.databricks.com/data/metastores/index.html)
+ [database](https://docs.databricks.com/data/tables.html)
data-store.databricks.azure.cloud
+ also known as data-source
+ files, databases, *etc.*, are considered **data stores**.
Amazon-Redshift.data-store.databricks.azure.cloud
Amazon-S3.data-store.databricks.azure.cloud
Amazon-S3-Select.data-store.databricks.azure.cloud
Azure-Blob-Storage.data-store.databricks.azure.cloud
Azure-Data-Lake-Storage-Gen1.data-store.databricks.azure.cloud
Azure-Data-Lake-Storage-Gen2.data-store.databricks.azure.cloud
Azure-Cosmos-DB.data-store.databricks.azure.cloud
Azure-SQL-Data-Warehouse.data-store.databricks.azure.cloud
SQL-Databases-using-JDBC.data-store.databricks.azure.cloud
Binary-File.data-store.databricks.azure.cloud
Cassandra.data-store.databricks.azure.cloud
ElasticSearch.data-store.databricks.azure.cloud
Image.data-store.databricks.azure.cloud
Hive-Tables.data-store.databricks.azure.cloud
MLflow-Experiment.data-store.databricks.azure.cloud
MongoDB.data-store.databricks.azure.cloud
Oracle.data-store.databricks.azure.cloud
Avro-Files.data-store.databricks.azure.cloud
CSV-Files.data-store.databricks.azure.cloud
JSON-Files.data-store.databricks.azure.cloud
LZO-Compressed-Files.data-store.databricks.azure.cloud
Parquet-Files.data-store.databricks.azure.cloud
Zip-Files.data-store.databricks.azure.cloud
partitioning
+ [more](https://medium.com/@mrpowers/managing-spark-partitions-with-coalesce-and-repartition-4050c57ad5c4)
aws-glue-data-catalog
+ a process for cataloging data
data-catalog.databricks.azure.cloud
+ example: **AWS Glue Data Catalog**
+ the **columns** and the **columns types** for each table for each data-store
+ the **columns** and the **columns types** are infered by a **crawler** through **customized classifiers**. If none of the classifiers successfuly categorizes the data, **built-in** classifiers try do categorize the data (example: JSON)
+ the crawler writes the schema to the data-catalog/hive metastore
+ [more](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html)
global.table.databricks.azure.cloud
+ available across all clusters
local.table.databricks.azure.cloud
spark-cluster.azure.cloud
azure-devops.azure.cloud
+ version-control
+ project management
+ defect tracking
+ automated builds
+ automated releases
+ QA testing
amazon.cloud  
azure.cloud  
google.cloud  
alibaba.cloud  
oracle.cloud  
hypervisor
+ kernell virtuzlization enabler
docker
+ application container (OS)
+ all docker containers share the same host OS kernel (linux + diff linux distros)
+ docker is not a kernel virtualization, it is OS virtualization with a common kernel, it is app containerization
+ it is lighter than a VM: less time to boot, less mem
+ VMs require the Hypervisor on top of the host OS
+ UCs:
    + complex architecture where different components required different OS or library versions
    + changing architecture as it goes along
    + run each architectural component in it's own container, all a local system requires is docker, and the app will
    be executed. It's like creating a VM with communicating VMs
    + developping in containers allows ease of deployment to docker environments in the same OS kernell
kubernettes, docker sawrm, mesos (apache)
+ container orchestration tool
+ dev by google
+ can orchestrate multiple docker hosts, and multiple docker containers inside each docker host
+ kubernettes cluster:
    + set of docker hosts for example
terraform.hashicorp
+ automate it infrastructure
ansible.redhat
+ orchestration tool:
    + cloud application deployments
    + automate it infrastructure
express  
+ nodejs router
akka  
devops  
az.availability-zone  
data-sovereignty  
version-control  
SAFe.agile.methodology.team.development  
methodology.self.development  
dns.network  
vpn.network  
kernel.operating-system  
bios.operating-system  
virtual-memory.operating-system  
ssd.hardware  
ram.hardware  
routing.web-application  
page-lifecycle.web-application  
regex  
react  
redux  
web-pack  
rest.api  
first-party-application
    dev inside framework
third-party-application
    dev outside framework
framework  
durability  
replication    
port
proxy
+ reroute **some** web activity
+ only reroutes the browser
+ don't guarantee provacy or security
vpn
+ reroute all web activity
+ all applications are securely rerouted
+  guarantee provacy or security
firewall
ip
express-route
acid.operations.information-system
dml.operations.information-system
ddl.operations.information-system
crud.operations.information-system
+ spark-vs-pandas-vs-dask
    + spark
        + RDD Dataframe, distributed version of a pandas dataframe for large-scale data
    + pandas
        + plot
        + indices
    + dask
        + distributes pandas



-----
questions  
[ucs para rdds ao inves de dataframes?](https://databricks.com/blog/2016/07/14/a-tale-of-three-apache-spark-apis-rdds-dataframes-and-datasets.html#targetText=Conceptually%2C%20consider%20DataFrame%20as%20an,or%20a%20class%20in%20Java.)   
[data lave vs data warehouse?](https://fr.talend.com/resources/data-lake-vs-data-warehouse/)  
[dimensional data modelling in haddop?](https://sonra.io/2017/05/15/dimensional-modeling-and-kimball-data-marts-in-the-age-of-big-data-and-hadoop/)  

-----
exercises  
[Create a crawler and custom classifiers to infer the schema of a data-store source](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html)

-----  
training  
[Mastering Git](https://app.pluralsight.com/library/courses/mastering-git/table-of-contents)  
[Building Your First ETL Pipeline Using Azure Databricks](https://app.pluralsight.com/course-player?clipId=10b035a0-0acf-4513-8e13-ef8ae09a5bb6)  
[Microsoft Azure Architecture - Getting Started](https://app.pluralsight.com/course-player?clipId=379f2d9a-0470-4593-a1e3-586e6e55a667)  
Overview. Good after some experience.  
[Azure DevOps: Getting Started](https://app.pluralsight.com/library/courses/azure-devops-getting-started/table-of-contents)  
Cool but I don't have rights to create project...  
[Networking Fundamentals](https://app.pluralsight.com/paths/skills/networking-fundamentals)  
[Introduction to Regular Expression (Regex)](https://app.pluralsight.com/library/courses/regular-expression-introduction/table-of-contents)  