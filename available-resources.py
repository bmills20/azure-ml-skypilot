# List available VMs by quota in a region on Azure

from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential
import os
from dotenv import load_dotenv

load_dotenv()

subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
location = os.getenv('AZURE_LOCATION')

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)

# List quota information
usages = compute_client.usage.list(location)

for usage in usages:
    print(f"Resource: {usage.name.localized_value}")
    print(f"Limit: {usage.limit}")
    print(f"Current Value: {usage.current_value}")
    print("-------------------------------")
