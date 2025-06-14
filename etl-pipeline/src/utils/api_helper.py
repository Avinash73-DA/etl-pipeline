import requests

def refresh_zoho_token(client_id, client_secret, scope):
    url = "https://accounts.zoho.com/oauth/v2/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
        "scope": scope
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def fetch_paginated_data(url, headers, key="data", page_key="page", per_page=100, limit_pages=10):
    all_data = []
    page = 1

    while page <= limit_pages:
        params = {
            page_key: page,
            "per_page": per_page
        }
        res = requests.get(url, headers=headers, params=params)
        if res.status_code != 200:
            break
        json_data = res.json()
        page_data = json_data.get(key, [])
        if not page_data:
            break
        all_data.extend(page_data)
        page += 1
    return all_data
