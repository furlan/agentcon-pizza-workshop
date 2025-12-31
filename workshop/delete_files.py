import os
from dotenv import load_dotenv

# Azure SDK imports
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import FilePurpose

# Load environment variables (expects PROJECT_CONNECTION_STRING in .env)
load_dotenv(override=True)

project_client = AIProjectClient(
    endpoint=os.environ["PROJECT_CONNECTION_STRING"],
    credential=DefaultAzureCredential()
)

print("Fetching all files from Azure Foundry...")
files = project_client.agents.files.list()

file_list = list(files)
print(f"Found {len(file_list)} files to delete.")

if not file_list:
    print("No files found in Azure Foundry.")
else:
    deleted_count = 0
    for file_id in file_list:
        try:
            project_client.agents.files.delete(file_id)
            print(f"Deleted file: {file_id}")
            deleted_count += 1
        except Exception as e:
            print(f"Error deleting file {file_id}: {e}")
    
    print(f"\nSuccessfully deleted {deleted_count} out of {len(file_list)} files.")