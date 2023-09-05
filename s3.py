import boto3
import botocore

import json
import requests
import json
from pkg_resources import resource_filename


def get_region_descriptions():
    result = {}
    # Source: https://github.com/boto/botocore/blob/develop/botocore/data/endpoints.json
    endpoint_file = resource_filename("botocore", "data/endpoints.json")
    with open(endpoint_file, "r") as f:
        endpoints = json.load(f)
        for partition in endpoints["partitions"]:
            for region in partition["regions"]:
                # Skip secret and Chinese regions
                if "us-iso" not in region and not region.startswith("cn-"):
                    result[partition["regions"][region]["description"]] = region
    return result


def download_s3_pricing():
    # Replace with the actual URL
    url = "https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonS3/current/index.json"

    # Download the file from the URL
    response = requests.get(url)

    # Check if the download was successful
    if response.status_code == 200:
        # Parse the JSON content
        data = json.loads(response.text)

        # Your parsing logic here, e.g., populate output_dict
        return data

    else:
        print(f"Failed to download file, status code: {response.status_code}")


def fetch_s3_pricing(regions, storage_data):
    # Initialize the output dictionary
    output_dict = {}
    data = download_s3_pricing()

    # Iterate through products to get metadata
    for sku, product_info in data["products"].items():
        print(sku, product_info)
        if "fromLocation" in product_info["attributes"].keys():
            region = product_info["attributes"]["fromLocation"]
        else:
            region = product_info["attributes"]["location"]
        product_description = product_info["attributes"]["usagetype"]
        print(region)
        print(product_description)

        # Initialize the region in the output dictionary if not already present
        if region not in output_dict:
            output_dict[region] = {}

        # Iterate through terms to get pricing info
        term_info = data["terms"].get("OnDemand", {}).get(sku, {})
        for term_key, term_values in term_info.items():
            price_dimensions = term_values.get("priceDimensions", {})
            for price_key, price_values in price_dimensions.items():
                price = price_values.get("pricePerUnit", {}).get("USD", "Unknown")

                # Add product and price to the region in the output dictionary
                output_dict[region][product_description] = price

    return output_dict


def scrape():
    storage_data = {"provider": "aws", "regions": {}}

    regions = get_region_descriptions().values()
    pricing = fetch_s3_pricing(regions, storage_data)

    # Write the output_dict to a JSON file
    with open("parsed_s3_offer_file.json", "w") as f:
        json.dump(pricing, f, indent=4)


if __name__ == "__main__":
    scrape()
