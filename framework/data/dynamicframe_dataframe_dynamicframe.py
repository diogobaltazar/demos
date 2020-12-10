import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.types import StringType
from pyspark.sql import functions as F


## @params: [TempDir, JOB_NAME]
args = getResolvedOptions(sys.argv, ['TempDir','JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "clean-s3-gluecatalogue-cmcmd", table_name = "test_results_csv", transformation_ctx = "DataSource0"]
## @return: DataSource0
## @inputs: []
DataSource0 = glueContext.create_dynamic_frame.from_catalog(
    database = "clean-s3-gluecatalogue-cmcmd",
    table_name = "test_results_csv",
    transformation_ctx = "DataSource0"
)

test_results = DataSource0.toDF()

test_results = test_results.select([
    F.col("nn").cast(StringType()),
    F.col("study_suite").cast(StringType()),
    F.regexp_replace(F.col("protocol").cast(StringType()), '\[|\]|,', '').alias('protocol'),
    F.col("study").cast(StringType()),
    F.col("material").cast(StringType()),
    F.col("project").cast(StringType()),
    F.col("batch").cast(StringType()),
    F.col("condition").cast(StringType()),
    F.col("time").cast(StringType()),
    F.col("time_days").cast(StringType()),
    F.col("method").cast(StringType()),
    F.col("parameter").cast(StringType()),
    F.col("parameter_type").cast(StringType()),
    F.col("result").cast(StringType()),
    F.col("unit").cast(StringType()),
    F.col("status").cast(StringType())
])

test_results = DynamicFrame.fromDF(test_results, glueContext, "test_results")
test_results.show()

## @type: DataSink
## @args: [database = "clean-redshift-gluecatalogue-cmcmd", redshift_tmp_dir = TempDir, table_name = "nnedlsandbox_cmc_aim_eln_testresult", transformation_ctx = "DataSink0"]
## @return: DataSink0
## @inputs: [frame = Transform0]
DataSink0 = glueContext.write_dynamic_frame.from_catalog(
    frame = test_results,
    database = "clean-redshift-gluecatalogue-cmcmd",
    redshift_tmp_dir = args["TempDir"],
    table_name = "nnedlsandbox_cmc_aim_eln_testresult",
    transformation_ctx = "DataSink0"
)
job.commit()
