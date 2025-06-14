import requests

def extract_custify_companies(api_token):
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    url = "https://api.custify.com/company/all"
    items_per_page, page, all_data = 100, 1, []

    while True:
        params = {"itemsPerPage": items_per_page, "page": page}
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            raise Exception(f"Custify API failed on page {page}, status: {response.status_code}")

        json_data = response.json()
        companies = json_data.get("data") or json_data.get("companies") or []
        if not companies:
            break

        all_data.extend(companies)
        page += 1

    return all_data