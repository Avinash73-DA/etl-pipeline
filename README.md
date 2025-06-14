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
🔹 extract/ – Data Ingestion Scripts
- extract_zoho.py – Extracts Credit Notes from Zoho API
- extract_hubspot.py – Extracts Deal Data from HubSpot
- extract_custify.py – Extracts Company Metrics from Custify

🔹 transform/ – Data Cleaning & Transformation
- transform_zoho.py – Normalizes Zoho data
- transform_hubspot.py – Cleans HubSpot pipeline data
- transform_custify.py – Transforms Custify API response

🔹 load/ – Data Loading into Delta Tables
- load_zoho.py – Loads Zoho data to Databricks
- load_hubspot.py – Loads HubSpot deals to target tables
- load_custify.py – Pushes Custify data to Delta Lake

🔹 utils/ – Reusable Utilities
- spark_utils.py – Spark session & Delta helpers
- api_helpers.py – API authentication, pagination
- logging.py – Custom logging setup

🔹 config/ – Configuration & Secrets
- config.yaml – API tokens, table names, endpoints

🔹 Root Files
- main.py – Main pipeline runner

- requirements.txt – Python package dependencies

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

### 2️⃣ Configure config/config.yaml

zoho:
 - base_url: "https://www.zohoapis.com/billing/v1/creditnotes"
 - table: "zoho_creditnotes"

hubspot:
- access_token: "your-hubspot-token"
- table: "hubspot_deals"

custify:
- api_token: "your-custify-token"
- "custify_companies"

---

🔐 Secrets Management

- 🔒 Never hardcode API tokens or secrets
- ✅ Use Databricks Secrets in production
- ➕ Extend to more APIs (e.g., Jira, Salesforce)

## 👤 Authors & Maintainers

**[Avinash M]** – Business Analyst  
📧 Email: [avinashsolai@gmail.com]  
🔗 LinkedIn: [www.linkedin.com/in/avinash-m-va73] 

