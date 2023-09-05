import requests
import json


def fetch_azure_storage_pricing():
    storage_data = {"provider": "azure", "regions": {}}

    url = "https://prices.azure.com/api/retail/prices?$filter=serviceName eq 'Storage'"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to get data: {response.status_code}")
        return

    data = response.json()

    for item in data["Items"]:
        region = item["armRegionName"]
        if region not in storage_data["regions"]:
            storage_data["regions"][region] = {}

        dimensions = item["meterName"]
        price = item["retailPrice"]

        storage_data["regions"][region][dimensions] = price

    with open("storage.json", "w") as f:
        json.dump(storage_data, f, indent=4)


if __name__ == "__main__":
    fetch_azure_storage_pricing()
