# 🔄 ETL Data Pipeline for Zoho, HubSpot & Custify

A modular ETL pipeline using **PySpark**, built to extract data from Zoho, HubSpot, and Custify APIs, transform it, and load it into Delta Lake.

---

## 📁 Project Structure

```bash
your-etl-project/
├── extract/
│   ├── extract_zoho.py
│   ├── extract_hubspot.py
│   └── extract_custify.py
│
├── transform/
│   ├── transform_zoho.py
│   ├── transform_hubspot.py
│   └── transform_custify.py
│
├── load/
│   ├── load_zoho.py
│   ├── load_hubspot.py
│   └── load_custify.py
│
├── utils/
│   ├── spark_utils.py
│   ├── api_helpers.py
│   └── logging.py
│
├── config/
│   └── config.yaml
│
├── main.py
└── requirements.txt
⚙️ Technologies Used
Python

PySpark

Delta Lake

REST APIs (Zoho, HubSpot, Custify)

YAML (for configuration)

Modular ETL Architecture

🔌 Data Sources
Source	Method	Purpose
Zoho	REST API	Finance credit notes
HubSpot	REST API	Deals pipeline data
Custify	REST API	Customer health and metrics

📦 How to Run
1️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
2️⃣ Configure config/config.yaml
Add your API tokens, base URLs, and destination table names:

yaml
Copy
Edit
zoho:
  base_url: "https://www.zohoapis.com/billing/v1/creditnotes"
  table: "finance_revops.finance_reports.zoho_creditnotes"

hubspot:
  access_token: "your-hubspot-token"
  table: "hubspot_deals"

custify:
  api_token: "your-custify-token"
  table: "finance_revops.sandbox.custify_companies"
✅ Optionally, use .env files for storing secrets and load them using dotenv.

3️⃣ Run the Pipeline
bash
Copy
Edit
python main.py
🔁 ETL Flow Diagram
mermaid
Copy
Edit
flowchart LR
    subgraph Extraction
        ZOHO[Zoho API]
        HUB[HubSpot API]
        CUS[Custify API]
    end

    subgraph Transformation
        TZO[Transform Zoho]
        THU[Transform HubSpot]
        TCUS[Transform Custify]
    end

    subgraph Load
        LZO[Load to Delta Table - Zoho]
        LHU[Load to Delta Table - HubSpot]
        LCUS[Load to Delta Table - Custify]
    end

    ZOHO --> TZO --> LZO
    HUB --> THU --> LHU
    CUS --> TCUS --> LCUS
🔐 Secrets Management
✅ Avoid hardcoding secrets.
✅ Use .env locally and Databricks secrets in production for security.

📘 Future Enhancements
✅ Add Airflow orchestration

✅ Unit testing and validation

✅ CI/CD via GitHub Actions

✅ Support more APIs (Jira, Salesforce, etc.)

👨‍💻 Author
Avinash M
Data Engineer & Business Analyst



📄 License
This project is open-sourced under the MIT License.
