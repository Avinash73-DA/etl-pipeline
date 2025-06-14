from pyspark.sql import SparkSession

def get_spark(app_name="ETL Pipeline"):
    spark = SparkSession.builder \
        .appName(app_name) \
        .config("spark.sql.shuffle.partitions", "4") \
        .enableHiveSupport() \
        .getOrCreate()
    return spark

def write_delta_table(df, table_name, mode="overwrite"):
    df.write.format("delta") \
        .option("mergeSchema", True) \
        .mode(mode) \
        .saveAsTable(table_name)
