**high-level** The pipeline is orchestrated by a cloudera edge node, transfering data from an azure blob container to a teradata database table.


**azure**

+ crt/access blob storage
+ crt/access container in blob storage
+ crt key-vault service
+ crt storage-account in key-vault service
+ sync key-vault to databricks  
+ config the blob storage mount point
+ write data to the blob container
+ [check the file in the blob container]

**teradata**

+ crt pipeline control tbl
+ insert job row in the control tbl with the correct field values

**cloudera**

+ edit the script:
    + usr teradata access credentials
    + control tbl database
+ exec the script

-----
**low-level** A solution is to use the ABS service to expose data to external systems, in particular by mounting the blob service to the DBFS, so that the data is written as a `<az-blob>` inside a `<az-blob-container>` of a `<az-blob-storage-account>` through a `<az-data-factory>` that is scheduling the writing to the blob container through a notebook.

Mind that these resources must reside in a resource group that can be deployed to production, *i.e.*, TODO, so:

+ `<az-resource-group> = rgpazewdcommercial`

Having been written to the blob container, a script will be executed in a cloudera edge node which will transfer the blob data to teradata. The edge node is the gateway to communicate between ADLS and on-premisses teradata.

Below, a detailed demonstration with concrete examples valid at the date of this post.

All of the below is related to the resource-group:

+ `<az-blob> = commercialblobdev`
+ `<az-blob-container> = inlanddailydriver`
+ `<az-blob-container-public-access-level> = Container (anonymous read access for containers and blobs)`
+ `<az-storage-account> = TODO`
+ `<az-storage-account-type> = Storage (general purpose v1)`
+ `<az-data-factory> = eval-comm-platform2-adf`

create ADO pipeline associated with the repository:

+ `<az-ado-organization> = diogopereiramarques`
+ `<az-ado-project> = idd`
+ `<az-ado-repo> = idd-ADB`
+ `<az-ado-pipeline-repo> = idd-ADB`

Adding to the repo the *devopsfile.yml* file:

```bash
# Python package
# Create and test a Python package on multiple Python versions.
# Add steps that analyze code, save the dist with the build record, publish to a PyPI-compatible index, and more:
# https://docs.microsoft.com/azure/devops/pipelines/languages/python

trigger:
- feature/scafolding

pool:
  vmImage: 'ubuntu-latest'
strategy:
  matrix:
    # Python27:
    #   python.version: '2.7'
    Python35:
      python.version: '3.5'
    # Python36:
    #   python.version: '3.6'
    # Python37:
    #   python.version: '3.7'

steps:
- task: CmdLine@2
  inputs:
    script: |
      ls -all -G
- task: UsePythonVersion@0
  inputs:
    versionSpec: '$(python.version)'
  displayName: 'Use Python $(python.version)'

- task: PipAuthenticate@1
  displayName: 'Pip Authenticate'
  inputs:
    # Provide list of feed names which you want to authenticate
    artifactFeeds: johan_test_ontology
    # Setting this variable to "true" will force pip to get distributions from official python registry first and fallback to feeds mentioned above if distributions are not found there.
    onlyAddExtraIndex: true

- script: |
    python -m pip install --upgrade pip
    pip install -r requirements.txt
  displayName: 'Install dependencies'

#- script: |
#    pip install pytest pytest-azurepipelines
#    pytest
#  displayName: 'pytest'

- task: CopyFiles@2
  displayName: 'Copy Files to: $(Build.ArtifactStagingDirectory)'
  inputs:
    SourceFolder: '$(Build.SourcesDirectory)'
    Contents: |
     **/*.py
     databricks.json
     requirements.txt
    TargetFolder: '$(Build.ArtifactStagingDirectory)'
    CleanTargetFolder: true
- task: PublishBuildArtifacts@1
  inputs:
    pathToPublish: $(Build.ArtifactStagingDirectory)
    artifactName: drop
```




TODO  

Create Key Vault:

+ `<az-key-vault> = ?`

end-points:

+ `<az-blob-storage-account-end-point> = http://<az-blob-storage-account>.blob.core.windows.net`
+ `<az-blob-container-end-point> = https://<az-blob>.blob.core.windows.net/<az-blob-container>`



+ `<cloudera-edge-node> = 10.18.76.36`
+ `<cloudera-edge-node-usr>`
+ `<cloudera-edge-node-pwd>`



Create a new blob container

-----

## resources

Place the resources below in your `~` dir in the edge node:

```bash
~ $ scp credentials.txt export.sh <cloudera-edge-node-usr>@<cloudera-edge-node>:/home/<cloudera-edge-node-usr>/
```

And run from the edge node:

```bash
~ $ . export.sh
```


*credentials.txt*

```bash
credentials: (sample contents of ~/azureaxsmod/credentials)
[default]
StorageAccountName = <az-storage-account>
StorageAccountKey  = <az-storage-account-key>
```

*export.sh*

```bash
usage () {
        echo "usage: TPT_JOB_SCRIPT.sh -v [Vertical]-j [JobName] -h [HostName]"
        echo " -v Vertical -j JobName -h HostName"
        echo " "
}

if [ $# -lt 6 ]; then
   echo " "
   echo "Invalid number of arguments"
   usage
   exit 1;
fi

# get Job Parameters
fn_getjobparam () {
        bteq<!>${PWD}/${JobName}_${PID}.log
        set echoreq off
        logon ${HostName}/${UserName},${Password};
        set titledashes off;
        set width 64000
        set format off

        export report file=${PWD}/${JobName}_${PID}.config

        locking row for access
        select
                TRIM(job_name)||'&'||
                TRIM(database_name)||'&'||
                TRIM(object_name)||'&'||
                TRIM(textdelimiter)||'&'||
                TRIM(coalesce(azprefix,''))||'/&'||
                TRIM(coalesce(azcontainer,'NA'))||'&'||
                TRIM(coalesce(azobject,'NA'))||'&'||
                TRIM(coalesce(azSinglePartFile,'NA'))||'&'||
                TRIM(SkipHeader)||'&'||
                TRIM(azConnectionCount) (title ' ')
        from <td-ctrl-db>.<td-strl-tbl>
        where TRIM(job_name)='${JobName}';

        export reset;


        quit;
        !

        export LogonStatus=`cat ${PWD}/${JobName}_${PID}.log|grep "RC (return code) = 8"|wc -l`

        if [ ${LogonStatus} -gt 0 ]; then
                echo "TPT Load Job Failed in STEP 1: Database Logons Failed"
                fn_cleanup
                fn_fcleanup
                exit 1;
        fi

        export JobNameDB=`cat ${PWD}/${JobName}_${PID}.config|awk -F"&" '{print $1}'`

        if [ -z "${JobNameDB}" ]; then
                echo "TPT Load Job Failed in STEP 1: Job Name ${JobName} Not Found in LabBICC_FBRaaS.tpt_control_tbl"
                fn_cleanup
                fn_fcleanup
                exit 1;
        else
                echo "STEP 1 Completed: Job Parameters Retrieved"
        fi

        export DatabaseName=`cat ${PWD}/${JobName}_${PID}.config|awk -F"&" '{print $2}'`
        export ObjectName=`cat ${PWD}/${JobName}_${PID}.config|awk -F"&" '{print $3}'`

        bteq<EOF>${PWD}/${JobName}_${PID}.dellog
        set echoreq off
        logon ${HostName}/${UserName},${Password};
        set titledashes off;
        set width 200
        set format off

        delete from ${DatabaseName}."${ObjectName}" all;

        quit;
        EOF

        export TextDelimiter=`cat ${PWD}/${JobName}_${PID}.config|awk -F"&" '{print $4}'`
        export azcontainer=`cat ${PWD}/${JobName}_${PID}.config|awk -F"&" '{print $6}'`
        export azprefix=`cat ${PWD}/${JobName}_${PID}.config|awk -F"&" '{print $5}'`
        export azSinglePartFile=`cat ${PWD}/${JobName}_${PID}.config|awk -F"&" '{print $8}'`
        export azConnectionCount=`cat ${PWD}/${JobName}_${PID}.config|awk -F"&" '{print $10}'`
        export azobject=`cat ${PWD}/${JobName}_${PID}.config|awk -F"&" '{print $7}'`
        export skiprow=`cat ${PWD}/${JobName}_${PID}.config|awk -F"&" '{print $10}'`

        if [ ${azprefix} == "/" ]; then
                export AccessModuleInitStr="-Container ${azcontainer}  -Object ${azobject} -SinglePartFile ${azSinglePartFile} -ConnectionCount ${azConnectionCount}"
        else
                export AccessModuleInitStr="-Container ${azcontainer}  -Object ${azobject} -Prefix ${azprefix} -SinglePartFile ${azSinglePartFile} -ConnectionCount ${azConnectionCount}"
        fi
}

# get Column DataTypes
fn_getcoltype () {
        bteq<EOF>${PWD}/${JobName}_${PID}.log
        set echoreq off
        ${BTEQLogonMech}
        logon ${HostName}/${UserName},${Password};
        set titledashes off;
        set width 5000
        set format off

        export report file=${PWD}/${JobName}_${PID}.collist


        select
                trim(columnname) (title ''),
                trim(columntype)(title ''),
                trim(columnlength)(title '')
        from dbc.columnsv
        where
                databasename='${DatabaseName}'
                and tablename='${ObjectName}'
        order by columnid;

        export reset;

        quit;
        EOF

        if [ ! -s ${PWD}/${JobName}_${PID}.collist ]; then
                echo "STEP 2 Failed: Object Validation "
                echo "Object ${DatabaseName}.${ObjectName} doesn't exist"
                echo " "
                fn_cleanup
                fn_fcleanup
                exit 3;
        fi

        cat ${PWD}/${JobName}_${PID}.collist|while read line
        do
                export DataType=`echo $line|awk '{print $2}'`
                if [ ${DataType} == "BV" ] || [ ${DataType} == "CF" ] || [ ${DataType} == "CV" ]; then
                        export ColLength=`echo $line|sed 's/,//g'|awk '{print $3}'`
                else
                        export ColLength="500"
                fi
                echo $line|sed 's/,//g'|awk -v q='"' '{print q $1 q "|" '${ColLength}' }' >> ${PWD}/${JobName}_${PID}.coltype
        done

        export ApplyList=`cat ${PWD}/${JobName}_${PID}.coltype|awk -F"|" '{print $1 ","}'|xargs -d '\n'|sed 's/.$//'`
        export ValueList=`cat ${PWD}/${JobName}_${PID}.coltype|awk -F'|' '{print ":" $1 ","}'|xargs -d '\n'|sed 's/.$//g'`

        if [ ! -s ${PWD}/${JobName}_${PID}.coltype ]; then
                echo "STEP 2: Column Datatype file creation failed"
                echo " "
                fn_cleanup
                fn_fcleanup
                exit 3;
        else
                echo "STEP 2 Completed: Column datatypes Retrieved"
        fi
}

# create TPT Schema
fn_createschema () {
        cat ${PWD}/${JobName}_${PID}.coltype|while read line
        do
                echo $line|awk -F"|" '{print " " $1"   VARCHAR("$2"),"}' >> ${PWD}/${JobName}_${PID}.schema1
        done
        cat ${PWD}/${JobName}_${PID}.schema1|sed '$ s/.$//' > ${PWD}/${JobName}.schema
        if [ ! -s ${PWD}/${JobName}.schema ]; then
                echo "STEP 3 Failed: TPT Schema creation failed"
                fn_cleanup
                fn_fcleanup
        else
                echo "STEP 3 Completed: TPT Schema Creation"
        fi
}

# Create TPT Schema
fn_createschema () {
        cat ${PWD}/${JobName}_${PID}.coltype|while read line
        do
                echo $line|awk -F"|" '{print " " $1"   VARCHAR("$2"),"}' >> ${PWD}/${JobName}_${PID}.schema1
        done
        cat ${PWD}/${JobName}_${PID}.schema1|sed '$ s/.$//' > ${PWD}/${JobName}.schema
        if [ ! -s ${PWD}/${JobName}.schema ]; then
                echo "STEP 3 Failed: TPT Schema creation failed"
                fn_cleanup
                fn_fcleanup
        else
                echo "STEP 3 Completed: TPT Schema Creation"
        fi
}

#  Create TPT Script
fn_tptload () {
        echo "
        define job SAMPLE_FILE_LOAD
        description 'Load a Teradata table from a file'
        (
                define schema SCHEMA_${JobName}
                (" > ${PWD}/${JobName}.tptld
        cat ${PWD}/${JobName}.schema >> ${PWD}/${JobName}.tptld
        echo "        );

                DEFINE OPERATOR op_${JobName}
                TYPE DATACONNECTOR PRODUCER
                SCHEMA SCHEMA_${JobName}
                ATTRIBUTES
                (
                VARCHAR AccessModuleName       = 'libazureaxsmod.so',
                                VARCHAR AccessModuleInitStr    = '${AccessModuleInitStr}',
        VARCHAR Format = 'Delimited',
                VARCHAR OpenMode = 'Read',
                VARCHAR TextDelimiter ='${TextDelimiter}',
                INTEGER SkipRows=${skiprow}
                );

                DEFINE OPERATOR ol_${JobName}
                TYPE UPDATE
                SCHEMA *
                ATTRIBUTES
                (
                        VARCHAR PrivateLogName = '${JobName}_PrivateLog',
                        VARCHAR TdpId = '${HostName}',
                        VARCHAR UserName = '${UserName}',
                        VARCHAR UserPassword = '${Password}',
                        VARCHAR WorkingDatabase = '${DatabaseName}',
                        VARCHAR LogTable = 'LabBICC_FBRaaS.${ObjectName}_LOG',
                        VARCHAR ErrorTable1 = 'LabBICC_FBRaaS.${ObjectName}_ET1',
                        VARCHAR ErrorTable2 = 'LabBICC_FBRaaS.${ObjectName}_ET2',
                        VARCHAR WorkTable = 'LabBICC_FBRaaS.${ObjectName}_WT',
                        VARCHAR TargetTable = '"'"'"${ObjectName}"'"'"'
                );

                STEP stLOAD_FILE_NAME
                (
                        APPLY
                        ('INSERT INTO  ${DatabaseName}."'"'${ObjectName}'"'" ( "${ApplyList}" )
                        VALUES ( "${ValueList}"
                        );')
                TO OPERATOR (ol_${JobName})
                        SELECT * FROM OPERATOR(op_${JobName});
                );
        );" >> ${PWD}/${JobName}.tptld

        if [ ! -s ${PWD}/${JobName}.tptld ]; then
                echo " "
                echo "STEP 4 Failed: TPT Load Script Creation Failed"
                echo " "
                fn_cleanup
                fn_fcleanup
                exit 5;
        else
                echo "STEP 4 Completed: TPT Load Script Creation "
        fi

        tbuild -f ${PWD}/${JobName}.tptld -j ${JobName}_${PID} > ${PWD}/${JobName}_${PID}.tptlog1
        export ErrorCount=`cat ${PWD}/${JobName}_${PID}.tptlog1|egrep 'Compilation failed due to errors|TPT Exit code set to 12|Job script compilation failed|Error:|terminated \(status 12\)|terminated \(status 8\)'|wc -l`
        if [ ${ErrorCount} -gt 0 ]; then
                echo "STEP 6 Failed: TPT Load Job Failed to Start for ${JobName}"
                echo " "
                cat ${PWD}/${JobName}_${PID}.tptlog1
                echo " "
                fn_jobstatus
                exit 6;
        fi

}

fn_jobstatus () {
        export azFileSize=`cat ${PWD}/${JobName}_${PID}.tptlog1 | grep "EOF Statistics" | awk '{print $5}'`
        export azFileTransferTime=`cat ${PWD}/${JobName}_${PID}.tptlog1 | grep "EOF Statistics" | awk '{print $13}'`
        export JobLog=`cat ${PWD}/${JobName}_${PID}.tptlog1 | grep "Job log:" | awk '{print $3}'`
        tlogview -l ${JobLog} -f TWB_EVENTS -o ${PWD}/${JobName}_${PID}.tptlog
        export JobStartTime=`cat ${PWD}/${JobName}_${PID}.tptlog | grep OperatorEnter | awk -F"," '{print $9}'`
        export RowsInserted=`cat ${PWD}/${JobName}_${PID}.tptlog | grep UpdateRowsInserted | awk -F"," '{print $9}'`
        export RowsUpdated=`cat ${PWD}/${JobName}_${PID}.tptlog | grep UpdateRowsUpdated | awk -F"," '{print $9}'`
        export RowsDeleted=`cat ${PWD}/${JobName}_${PID}.tptlog | grep UpdateRowsDeleted | awk -F"," '{print $9}'`
        export ETRows=`cat ${PWD}/${JobName}_${PID}.tptlog | grep UpdateETRows | awk -F"," '{print $9}'`
        export UVRows=`cat ${PWD}/${JobName}_${PID}.tptlog | grep UpdateUVRows | awk -F"," '{print $9}'`
        export CPUTime=`cat ${PWD}/${JobName}_${PID}.tptlog | grep CPUTimeByInstance | awk -F"," '{print $9}'`
        export JobEndTime=`cat ${PWD}/${JobName}_${PID}.tptlog | grep OperatorEndTS | awk -F"," '{print $9}'`
        export JobStatusCnt=`cat ${PWD}/${JobName}_${PID}.tptlog | grep RDBMSError | wc -l`

        if [ ${ErrorCount} == 0 ]; then
                export JobStatus="Success"
                export ErrorCode=0
                export ErrorText="NULL"
                fn_loadlogdtl
                fn_echolog "TPT Load Job Completed Successfully for ${JobName}"
                fn_cleanup
        else
                export JobStatus="Failed"
                export ErrorCode=`cat ${PWD}/${JobName}_${PID}.tptlog|grep RDBMSError|awk -F"," '{print $9}'`
                export ErrorText=`cat ${PWD}/${JobName}_${PID}.tptlog|grep RDBMSMsgTxt|awk -F"," '{print $9}'|sed "s/'//g"`
                fn_loadlogdtl
                fn_echolog "TPT Load Job Failed for ${JobName}"
                fn_cleanup
                fn_fcleanup
                exit 7;
        fi
}

fn_loadlogdtl () {
        bteq<<EOF>${PWD}/${JobName}_${PID}.loadlog
        set echoreq off
        logon ${HostName}/${UserName},${Password};
        set titledashes off;
        set width 6000
        set format off

        insert into <td-ctrl-db>.<td-strl-tbl>
        values (
                CURRENT_DATE,
                '${JobName}',
                'LOAD',
                '${PID}',
                '${DatabaseName}',
                '${ObjectName}',
                '${azcontainer}',
                '${azprefix}',
                '${azobject}',
                '${azFileSize}',
                '${azFileTransferTime}',
                '${JobStartTime}',
                '${ExportedRows}',
                '${RowsInserted}',
                '${RowsUpdated}',
                '${RowsDeleted}',
                '${ErrTable1Rows}',
                '${ETRows}',
                '${ErrTable2Rows}',
                '${UVRows}',
                '${RejectedRows}',
                '${CPUTime}',
                '${JobEndTime}',
                '${JobStatus}',
                '${ErrorCode}',
                '${ErrorText}',
                CURRENT_TIMESTAMP
        );

        quit;
        EOF
        export JobStatus=`cat ${PWD}/${JobName}_${PID}.loadlog | grep "RC (return code)" | awk -F"= " '{print $2}'`
        if [ ${JobStatus} != 0 ]; then
                echo "Job Log Table Load Failed: Job Name - ${JobName}"
                cat ${PWD}/${JobName}_${PID}.loadlog
                fn_cleanup
                fn_fcleanup
        fi
}

fn_echolog () {
        echo $1

        if [ -f ${PWD}/${JobName}_${PID}.tptlog1 ]; then
            echo "Please find TPT Log for more details"
            cat ${PWD}/${JobName}_${PID}.tptlog1
        fi
}

fn_cleanup () {
        rm -rf ${JobLog}
        rm -rf ${PWD}/${JobName}_${PID}*
}

fn_fcleanup () {
        rm -rf ${PWD}/${JobName}*
}

while getopts v:j:h: name; do
      case $name in
     
	  v)    Vertical=$OPTARG;
              export Vertical
              ;; 
	  
      j)      JobName=$OPTARG;
              export JobName
              ;;
      h)      HostName=$OPTARG;
              export HostName
              ;;
      \?)     usage
              return 1
              ;;
      esac
done

if [ ${Vertical} == "COM" ]; then 
        export UserName="<usr>"
        export Password="<pwd>"
fi

export PID=$$
fn_getjobparam
fn_getcoltype
fn_createschema
fn_tptload
fn_jobstatus
fn_fcleanup
```

-----

## doc

ABS Azure Blob Service 
[src-1](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction#:~:targetText=Block%20blobs%20store%20text%20and,that%20can%20be%20managed%20individually.&targetText=Page%20blobs%20store%20random%20access,disks%20for%20Azure%20virtual%20machines.) |
[src-2](https://docs.microsoft.com/fr-fr/azure/databricks/data/data-sources/azure/azure-storage)  
DBFS Databricks File System [src-1](https://docs.databricks.com/data/databricks-file-system.html)  
ASC Azure Storage Account [src-1](https://docs.microsoft.com/en-us/azure/storage/common/storage-account-overview)  
AKV Azure Key Vault [src-1](https://azure.microsoft.com/en-us/services/key-vault/)