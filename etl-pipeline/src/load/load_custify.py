# --- load/load_custify.py ---
def load_custify_data(spark, df):
    sdf = spark.createDataFrame(df)
    sdf = sdf.select([col(c).cast("string") for c in sdf.columns])
    sdf.createOrReplaceTempView("custify_companies")
    sdf.write.format("delta").mode("overwrite").option("mergeSchema", "true").option("comment", "Custify companies full refresh").saveAsTable("custify_companies")
