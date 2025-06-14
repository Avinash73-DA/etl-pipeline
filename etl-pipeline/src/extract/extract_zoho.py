# extract_zoho.py
import requests
import json

def extract_zoho_creditnotes(client_id, client_secret, org_id):
    token_url = "https://accounts.zoho.com/oauth/v2/token"
    scope = "ZohoSubscriptions.creditnotes.READ"
    token_data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
        "scope": scope
    }

    response = requests.post(token_url, data=token_data)
    if response.status_code != 200:
        raise Exception(f"Token Request Failed: {response.status_code} - {response.text}")

    access_token = response.json()["access_token"]
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}",
        "X-com-zoho-subscriptions-organizationid": org_id
    }

    base_url = "https://www.zohoapis.com/billing/v1/creditnotes"
    page, per_page, all_data = 1, 200, []

    while True:
        url = f"{base_url}?page={page}&per_page={per_page}"
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            raise Exception(f"Data Request Failed on Page {page}: {res.status_code} - {res.text}")

        data = res.json().get("creditnotes", [])
        if not data:
            break

        all_data.extend(data)
        page += 1

    return all_data