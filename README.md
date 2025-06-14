# 🚀 Modular ETL Pipeline Using PySpark, Delta Lake & REST APIs

This repository documents an end-to-end ETL (Extract, Transform, Load) pipeline for integrating and processing data from **Zoho**, **HubSpot**, and **Custify** using **PySpark**, **Delta Lake**, and **REST APIs**.

---

## 📌 Project Overview

The pipeline follows a clean, modular structure with three distinct phases:

- **Extraction**: API data from Zoho (Credit Notes), HubSpot (Deals), Custify (Company metrics)  
- **Transformation**: Data cleaning and normalization with PySpark  
- **Loading**: Writes into Databricks Delta tables for analysis

---

## 📁 Project Structure

  ├── extract/
  │ ├── extract_zoho.py
  │ ├── extract_hubspot.py
  │ └── extract_custify.py
  │
  ├── transform/
  │ ├── transform_zoho.py
  │ ├── transform_hubspot.py
  │ └── transform_custify.py
  │
  ├── load/
  │ ├── load_zoho.py
  │ ├── load_hubspot.py
  │ └── load_custify.py
  │
  ├── utils/
  │ ├── spark_utils.py
  │ ├── api_helpers.py
  │ └── logging.py
  │
  ├── config/
  │ └── config.yaml
  │
  ├── main.py
  └── requirements.txt


---

## ⚙️ Technologies Used

- 🐍 Python  
- 🔥 PySpark  
- 💾 Delta Lake  
- 🌐 REST APIs (Zoho, HubSpot, Custify)  
- ⚙️ YAML for configuration  
- 🧱 Modular architecture  

---

## 🔌 Data Sources

| Source   | Method    | Purpose                     |
|----------|-----------|-----------------------------|
| Zoho     | REST API  | Finance Credit Notes        |
| HubSpot  | REST API  | Deals Pipeline              |
| Custify  | REST API  | Customer Health & Metrics   |

---

## ▶️ How to Run

### 1️⃣ Install Dependencies
pip install -r requirements.txt


---

## ⚙️ Technologies Used

- 🐍 Python  
- 🔥 PySpark  
- 💾 Delta Lake  
- 🌐 REST APIs (Zoho, HubSpot, Custify)  
- ⚙️ YAML for configuration  
- 🧱 Modular architecture  

---

## 🔌 Data Sources

| Source   | Method    | Purpose                     |
|----------|-----------|-----------------------------|
| Zoho     | REST API  | Finance Credit Notes        |
| HubSpot  | REST API  | Deals Pipeline              |
| Custify  | REST API  | Customer Health & Metrics   |

---

## ▶️ How to Run

### 1️⃣ Install Dependencies

bash
pip install -r requirements.txt

---

2️⃣ Configure config/config.yaml

zoho:
  base_url: "https://www.zohoapis.com/billing/v1/creditnotes"
  table: "finance_revops.finance_reports.zoho_creditnotes"

hubspot:
  access_token: "your-hubspot-token"
  table: "hubspot_deals"

custify:
  api_token: "your-custify-token"
  table: "finance_revops.sandbox.custify_companies"
  ✅ Optionally, use .env files for storing secrets and load them using python-dotenv.

---

  3️⃣ Run the Pipeline
  python main.py
  
---
🔐 Secrets Management

✅ Never hardcode API tokens or secrets.

✅ Use .env locally

✅ Use Databricks Secrets in production

🚧 Future Enhancements

⏱ Add Airflow orchestration

✅ Unit testing and validation

🔄 CI/CD via GitHub Actions

🧩 Extend to more APIs (Jira, Salesforce)

👨‍💻 Author
Avinash M – Data Engineer & Business Analyst
📧 Email: avinashsolai@gmail.com
🔗 LinkedIn: linkedin.com/in/avinash-m-va73


