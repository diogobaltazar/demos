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
lineage-graph.computation.dataset  
+ enables:
+ data lineage
+ fault-recovery by recalculating through the lineage graph should data be missing/corrupted
data-lineage  
fault-tolerant  
elastic-search  
relational-database  
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
dataframe.distributed.system
+ tabular schema API on top of RDD
+ with tabular schema: ++performance
sparksql.spark.distributed.system
    + structured data processing: pyspark, etc.
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
standard-spark-cluster.spark-cluster.databricks.azure.cloud
+ different users share single cluster and it's resources
databricks-serverless.spark-cluster.databricks.azure.cloud
+ a spark-cluster designed for high concurrency
+ each user accesses a shared pool of resources, granting isolation for the user spark environment
delta-lake.databricks.azure.cloud
+ a data lake is difficult to manage
+ open-source storage layer that adds features/structure to data lake files:
    + ACID operations over the same file
    + schema enforcement
    + full dml support
    + rollback
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
kubernettes  
express  
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
firewall
ip
express-route
acid.operations.information-system
dml.operations.information-system
ddl.operations.information-system
crud.operations.information-system
-----
questions  
ucs para rdds ao inves de dataframes?  

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