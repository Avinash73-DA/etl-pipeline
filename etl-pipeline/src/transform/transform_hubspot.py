# --- transform/transform_hubspot.py ---
from pyspark.sql.functions import col, to_timestamp, from_utc_timestamp, to_date, regexp_replace, weekofyear, current_date
from pyspark.sql.types import StringType

def transform_hubspot_data(spark, df):
    df_clean = df.withColumn("closedate_clean", regexp_replace("closedate", r"\.\d{3}", ""))\
                 .withColumn("createdate_clean", regexp_replace("createdate", r"\.\d{3}", ""))

    df_transformed = df_clean.withColumn("closedate_ist_ts", from_utc_timestamp(to_timestamp(col("closedate_clean"), "yyyy-MM-dd'T'HH:mm:ssX"), "Asia/Kolkata"))\
                              .withColumn("closedate_ist_date", to_date("closedate_ist_ts"))\
                              .withColumn("createdate_ist_ts", from_utc_timestamp(to_timestamp(col("createdate_clean"), "yyyy-MM-dd'T'HH:mm:ssX"), "Asia/Kolkata"))\
                              .withColumn("createdate_ist_date", to_date("createdate_ist_ts"))\
                              .withColumn("current_week", weekofyear(current_date()))

    df_casted = df_transformed.select([col(c).cast(StringType()).alias(c) for c in df_transformed.columns])
    return df_casted