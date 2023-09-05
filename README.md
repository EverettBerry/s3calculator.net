# Intro

S3 is not only a storage service offered by AWS but has become a de-facto standard and API specification for object storage. This webpage collects pricing information from major clouds which offer an S3-compatible object store. Where there is not an API, prices are hardcoded using publicly available documentation.

# Functionality

The calculator saves certain preferences (such as region or date bin) locally so that when the calculator is reloaded, settings are retained. Some dimensions have in-app documentation where you can mouseover to read more. The calculator works on mobile browsers.

Prices are available in a /storage.json file which can be downloaded. Each storage service has a detail page which shows expanded information such as data transfer rates, CDN integrations, links to documentation, and a "pivot" on the dropdowns available on the main page.

# Architecture

Prices are pulled daily from each cloud provider via Python. The prices are assembled into a storage.json file. The webpage is rendered using that file. The webpage is hosted on github pages. A github action runs each day to build the site.

# Supported Clouds

- AWS
- Azure
- Google Cloud
- Cloudflare

# Aspirational Features

- If you have a custom rate card, you can import those rates into the tool.
- You can email calculations to your self, or export them to a CSV/Excel file.
- You can enter your email to stay updated on pricing changes
- Historical prices are supported

# References

- [AWS Pricing API](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/pricing/client/describe_services.html)
- [AWS S3 Pricing](https://aws.amazon.com/s3/pricing/)
- [AWS S3 Bulk Pricing API](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonS3/current/index.json)
- [AWS S3 Deep Archive Bulk Pricing API](https://pricing.us-east-1.amazonaws.com/offers/v1.0/aws/AmazonS3GlacierDeepArchive/current/index.json)
- [Azure Retail Prices API](https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices)
- [Google Cloud Pricing API](https://cloud.google.com/billing/docs/reference/pricing-api/rest)
- [Google Cloud Storage Pricing](https://cloud.google.com/storage/pricing)
- [Backblaze B2 S3 compatibility](https://www.backblaze.com/b2/s3-compatibility.html)
- [Cloudflare R2 S3 compatibility](https://developers.cloudflare.com/r2/api/s3/api/)
