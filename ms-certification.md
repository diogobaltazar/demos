outlook usr: diogopm@outlook.com, OUTlook
data warehouse - historical information

-----

it's so easy to kick ass in IT with maths skilsl because there are so few people doing it. everyone is old, heavy and slow. and Im young, lithe and energetic. i have to keep repeating this to me to keep a notion of what I am, of my qualities, and not let myself go down when I met stronger people.

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
+ TLS for data in transaction/in transit
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
+ a user has many subscriptions
+ a usr has many storage accounts
+ blob is not hierarchical
+ data-lake (gen2) is a hierarchical blob
+ download storage explorer to interact with the datalke
+ data factory is an orchestrator, it can be used to extract data into the datalake
+ Can we usd the DF to ingest in real-time? No, go to EventHubs
+ Can cosmos DB replace SQL DW? CDB is for NoSQL. SQL DW reads the files from the DLake but does not crt them, it contains the schemas only.
+ PolyBase will read from the files and create schemas in the SQL DW
+ Are we going to create a SQL DW? How to access it? Client? 
+ Do you need to crt a SQL DW before writing the polyBase scripts?
+ Are we crting PolyBase scripts?
+ SQL DW has it's own memory that can store files?
+ When I do transformation on data in the datalake, the results are stored in SQL DW? Some might be. Only in the DW. The DW is for data ONLY relational.
+ SQL DB vs SQL DW? Differences?
+ IoT hubs vs Event Hubs vs Blob ?
+ sensors, IoT -> Apache Kafka/EventHubs/IoTHubs -> databricks/analysis services
+ media unstructured, files unstructured, logs -> data factory
+ PolyBase reads from the datalake
+ Polybase is always to capture data from unstructured sources
+ creating a DataLake Gen1 does not require crting a Storage Account, we crt itdirectly, not like DLakeGen2
+ DF: author and monitor
+ GEN1 : make the DF owner of this GEN1 by adding it as opwner
+ COPY DATA
+ Crt new connection
+ choose src dataset
+ choose binary data because gen2 takes bin data?!
+ Service Principal vs Account Key vs Managed Entity?
+ crt new connection for dest
+ access the file with the client for GEN2 and download it


## check
+ azure bot framework

## lab3
+ Cosmos DB GA: Global Availability, LRS locally, GA globally
    + high availability
    + GA, multi-master feature
    + LRS
    + good for unstrutured data, the DW cannot support this
    + migration difficult from DW to Cosmos DB, but Cosmos DB would have the same cost as DW if not GA
+ DONT FORGET to migrate from GEN1 to GEn2
+ create databricks workspace
+ create databricks cluster
+ schedule notebook 
+ connection to blob? by mounting it
+ connection to MySQL, Hive? JDBC -- **TODO**
+ The datasets in a nb are cached in memory? How to uncache them?
+ When I write a dataset to DBFS, where is it being written? Becauase it is being persisted... (see example)
+ broadcast vs standard joins
+ parquet best for databricks? how about avro?
+ why should we never use udfs?
+ a lot more of resources are created when creating the databriks workspace and cluster
+ distributed database with Cosmos DB
+ Cosmos DB is good because of scalability
+ auto creates indexes on the data
+ SPENDING
    + DBU - databricks unit
    + SYNAPSE ANA - DWU datawarehouse units
    + COSMOS - RU requests units
+ partition: always define a partition srtategy, how to define one? what are the metrics to dfine good partitioning?
+ crt cosmos db, with enabled multi-region
+ when should we use cosmos DB? When could it replace SQL DW?
+ create new container with partition key configured for the data that is going to be ingested
+ on cosmos DB / Data explorer / database / items / New Item
```json
{
    "partition_id": 2,
    "value": "2",
}

{
    "partition_id": 1,
    "value": "1",
}
```
+ Cosmos DB is a storage account like blob or data-lake
+ HOW TO mount data in Cosmos DB to databricks?
+ create stored procedure and specify partition type/value (Custom, 1)
```javascript
function createMyDocument() {
    var context = getContext();
    var collection = context.getCollection();
    var doc = {
        "partition_id": 1,  
    };
    var accepted = collection.createDocument(
        collection.getSelfLink(),
        doc,
        function (err, documentCreated) {
            if (err) throw new Error('Error' + err.message);
                context.getResponse().setBody(documentCreated)
        }
    );
    if (!accepted) return;
}
```
SEE VID on DATA SELF SERVICE

+ install .net sdk 3.1.101
+ isntall azure cosmos db vsc plugin
+ login and check the cosmos db in vsc
+ create new cosmos storage through vsc,s pecify the partition key which must coincide with the c# class for User
+ crt new directory in local fs to host the cs project 
+ open that dir in vsc
+ run `dotnet new console` which will create new dotnet app
+ isntall
```bash
dotnet add package System.Net.Http
dotnet add package System.Configuration
dotnet add package System.Configuration.ConfigurationManager
dotnet add package Microsoft.Azure.DocumentDB.Core
dotnet add package Newtonsoft.Json
dotnet add package System.Threading.Tasks
dotnet add package System.Linq
dotnet restore
```
+ add namespaces to ``:
```cs
using System;.
using System.Configuration;
using System.Linq;
using System.Threading.Tasks;
using System.Net;
using Microsoft.Azure.Documents;
using Microsoft.Azure.Documents.Client;
using Newtonsoft.Json;
```
+ crt new file `App.config` and add (getting the values with *right-click* over the created vsc cosmos db account)
```xml
<?xml version="1.0" encoding="utf-8"?>
    <configuration>
    <appSettings>
        <add key="accountEndpoint" value="https://vsccreatedaccountdpm.documents.azure.com:443/" />    <!--cosmos db connection string need to be capture.-->
        <add key="accountKey" value="9lPcYMK56uKxgJWoV4zoLiPoTOkBj2lgqynL1VBkG5Lv2AMFUUGeTXpBkVzJVzi9bYQzQWsvG5M6HFqY2pefIA" />
    </appSettings>
</configuration>
```
+ SEE CODE program.cs to ADD and GET
+ Auditing tab for managing database requests
+ theres not update in NoSQL, so its replace
+ consistency leves CosmosDB:
    + strong: reads are guaranteed to return the most recent version of an item
    + bounded staleness: reads lag behind writes
    + session: read follows the read
    + consistent prefix: no gap
    + eventual: out-of-order reads
+ change replication rules in cosmos DB / Replicate data globally

## lab4
+ azure SQL DB 
+ az synapse analytic 
+ ...

+ az SQL DB
    + DTU data transation unit
    + convenience: consume relational data, don't worry about the HW, SaaS
    + cost: set pricing
    + scale: scale size
    + security
+ if we do a transformation in a SQL DB, the data for the transformation RESIDES ONLY in the SQL DB, not in the data-lake
+ SQL server management studio to itneract with the SQL DB
+ DTU : db transaction unit computer, storage, io resources
+ transformations on BIG TABLES should be ran on SPARK CLUSTER, not on SQL DB
+ SQL resources elastic pool
+ CRT sql database
+ create server: dpm, P4ssw0rd
+ get the anme of the server `testsqldbserverdpm.database.windows.net` and login through the SQL SERVER MANAGEMENT CLIENT
+ on the first login, you have to register your IP, or at the SQL DB, add a new rule 0.0.0.0 - 255.255.255.255, there the connection is made
+ login with the database through the CLI: `sqlcmd -S tcp:testsqldbserverdpm.database.windows.net,1433 -d testsqldbdpm -U dpm -P 'P4ssw0rd'`
+ crt database:
```sql
1> create database testdclidbdpm
2> go
```
+ we're basically interactng with te SQL DB through the AZ CLI

## lab 5
synapse analytics
+ centralized server
+ spark engine
+ repakce the SQL DW by adding the features of
    + SPARK
    + data integration
+ will replace the SQL DW
+ SQL server + Hadoop
+ CRT synapse DB