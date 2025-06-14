def load_zoho_data(spark, df):
    spark_df = spark.createDataFrame(df)
    spark_df.write.format("delta").option("mergeSchema", True).mode("overwrite").saveAsTable("zoho_creditnotes")