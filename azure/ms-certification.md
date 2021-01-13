outlook usr: diogopm@outlook.com, OUTlook
data warehouse - historical information

-----

BI
+ SSIS - integration services (ETL processes)
+ SSAS - analysis services
+ SSRS - reporting services (SelfServiceBI: PowerBI, ExcelBI)
+ FACT - (foreign keys) measures, cols on which I can perform aggregations, numeric columns
+ DIMENSION - (primary keys) attributes (criteria on the basis of I'll analyse the data)

**example**  
company
+ revenue
+ geography_key

geography
+ country
+ key
+ revenue
+ tech_key

technology
+ name
+ revenue
+ key

## L1
### data abundance
telco has been generating huge amounts of data, structured, semi-structured and unstructured data).

+ **schema** applies a priori to data
+ **runtime schema** is inferenced at runtime

locale: culture specific + language

cloud vs on-premises advantages:
+ single licensing
+ maintenaince (upgrades)
+ scalability
+ availability

+ IaaS - 
+ PaaS - hosts the hardware and software on its own infrastructure, az SQL DB
+ SaaS - 

-----

new skills: structure and unstructured, not like DBAs
implmenting & provisioning: lift and shift (migrating to the cloud)
changing loading approaches: etl to elt

### use cases
web retail: amazon, ebay
healthcare: 
IoT: 

QUORUM: cluster manager

### databricks vs VS
+ databricks has concepts as *caching*, and we can't use that with the code in VS

Q01 - ingestion processes: ETL
Q02 - infer schema in statement: unstructured
Q03 - 

## L03: services
+ data lake
+ databricks
+ cosmos DB
+ sql DB
+ sql DW
+ stream analytics
+ more...

+ strcutured: tabular module
+ semi-structured: hierarchy tagged to lowest grane
+ unstrcutured: NoSQL
    + *depending on the purpose, choose your NoSQL*
    + key-value: same data type on all idnexes
    + document: json, xml
    + graph databases: 
    + column: TODO


+ **azure storage account**/**azure blob**/**data-lake** Massively scalable object store for text and binary data
    + UC: store data without need to query it directly (without frameworks)
    + UC: for streaming
    + data-lake-gen1 : stores data as files + 
    + data-lake-gen2 : stores data as files + blob with hierarchy
    + **security**: user profiles
    + redundancy
+ **azure files** managed file shares
+ **azure queues** TODO, messaging protocol for applications to communicate, the queue is a temp storage location from where msges can be sent or received
+ **azure tables** NoSQL

CosmosDB supports all these APIs:
+ SQL (tabular)
+ MongoDB (documents)
+ Cassandra (columnar)
+ Gremlin (graphs)
+ Table (blob)
99.999% availability

+ Azure OLTP: online transactional process (related to tabular data)
+ Azure OLAP: online analytical process (related to tabular and relational data)

secutiry on AZ SQL DB
+ TDE for data at rest (default)
    + encrypts
    + tracks who transformed what (not default)
+ TLS for data in transaction
+ DW: store historical data
    + costly: charged by hours

+ BCO : Bulk Copy Operation

+ EDA : exploratory data analysis
+ storage: share maximum of 8T
+ one storage account can only have one policy (question with the policies)

## lab1
a storage account is a **container**.
how to chose storage account:
+ data diversity: different data sources and different access profiles (for sensitivity)
+ cost sensitivity
+ management overhead

+ storage accounts have a cost only when a container is created
+ resources need to have unique ids worldwide
+ the subscription is unique for each user worlwide
+ if I choose activate data lake gen2, itll activate the data-lake
+ container is a type of storage account

## lab2
data-lake storage gen1, gen2
crt new storage account with gen2 (activer) 
install datalake explorer client

## takeawas
a user has many subscriptions
a usr has many storage accounts
blob is not hierarchical
data-lake (gen2) is a hierarchical blob
download storage explorer to interact with the datalke
data factory is an orchestrator, it can be used to extract data into the datalake
Can we usd the DF to ingest in real-time? No, go to EventHubs
Can cosmos DB replace SQL DW? CDB is for NoSQL. SQL DW reads the files from the DLake but does not crt them, it contains the schemas only.
PolyBase will read from the files and create schemas in the SQL DW
Are we going to create a SQL DW? How to access it? Client? 
Do you need to crt a SQL DW before writing the polyBase scripts?
Are we crting PolyBase scripts?
SQL DW has it's own memory that can store files?
When I do transformation on data in the datalake, the results are stored in SQL DW? Some might be. Only in the DW. The DW is for data ONLY relational.
SQL DB vs SQL DW? Differences?
+ IoT hubs vs Event Hubs vs Blob ?
sensors, IoT -> Apache Kafka/EventHubs/IoTHubs -> databricks/analysis services
media unstructured, files unstructured, logs -> data factory
PolyBase reads from the datalake
Polybase is always to capture data from unstructured sources
creating a DataLake Gen1 does not require crting a Storage Account, we crt itdirectly, not like DLakeGen2
DF: author and monitor
GEN1 : make the DF owner of this GEN1 by adding it as opwner
COPY DATA
Crt new connection
choose src dataset
choose binary data because gen2 takes bin data?!
Service Principal vs Account Key vs Managed Entity?
crt new connection for dest
access the file with the client for GEN2 and download it


## check
+ azure bot framework