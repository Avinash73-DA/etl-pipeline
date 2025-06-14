# --- load/load_hubspot.py ---
def load_hubspot_data(df):
    df.write.format("delta").mode("overwrite").option("mergeSchema", "true").saveAsTable("hubspot_deals")
