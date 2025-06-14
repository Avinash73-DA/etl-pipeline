# --- transform/transform_zoho.py ---
from pyspark.sql.functions import col

def transform_zoho_data(df):
    if "created_time" in df.columns:
        df["created_time"] = pd.to_datetime(df["created_time"]).dt.tz_localize(None)
    return df