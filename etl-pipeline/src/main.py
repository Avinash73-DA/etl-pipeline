from extract import extract_zoho, extract_hubspot, extract_custify
from transform import transform_zoho, transform_hubspot, transform_custify
from load import load_zoho, load_hubspot, load_custify

def main():
    print("🚀 Running ETL pipeline...")

    # ZOHO
    zoho_df = extract_zoho.run()
    zoho_transformed = transform_zoho.run(zoho_df)
    load_zoho.run(zoho_transformed)

    # HUBSPOT
    hubspot_df = extract_hubspot.run()
    hubspot_transformed = transform_hubspot.run(hubspot_df)
    load_hubspot.run(hubspot_transformed)

    # CUSTIFY
    custify_df = extract_custify.run()
    custify_transformed = transform_custify.run(custify_df)
    load_custify.run(custify_transformed)

    print("✅ ETL completed.")

if __name__ == "__main__":
    main()
