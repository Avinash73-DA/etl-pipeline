# extract_hubspot.py
from hubspot import HubSpot
from hubspot.crm.deals import Filter, FilterGroup, PublicObjectSearchRequest

def extract_hubspot_deals(access_token):
    client = HubSpot(access_token=access_token)
    all_deals = []
    after = None

    while True:
        forecast_filter = Filter(
            property_name="hs_manual_forecast_category",
            operator="NEQ",
            value="OMIT"
        )
        filter_group = FilterGroup(filters=[forecast_filter])

        search_request = PublicObjectSearchRequest(
            filter_groups=[filter_group],
            properties=[
                "amount", "hs_manual_forecast_category", "dealname",
                "hubspot_owner_id", "closedate", "dealstage", "createdate", "pipeline"
            ],
            limit=100,
            after=after
        )

        response = client.crm.deals.search_api.do_search(public_object_search_request=search_request)
        all_deals.extend(response.results)

        if not response.paging or not response.paging.next:
            break
        after = response.paging.next.after

    return all_deals