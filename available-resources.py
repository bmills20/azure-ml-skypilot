# List available VM sizes in a region on Azure

from azure.mgmt.compute import ComputeManagementClient
from azure.identity import DefaultAzureCredential
import os
from dotenv import load_dotenv

load_dotenv()

subscription_id = os.getenv('AZURE_SUBSCRIPTION_ID')
location = os.getenv('AZURE_LOCATION')

credential = DefaultAzureCredential()
compute_client = ComputeManagementClient(credential, subscription_id)

vm_sizes = compute_client.virtual_machine_sizes.list(location)

for size in vm_sizes:
    print(size.name)