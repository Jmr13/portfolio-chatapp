import os
from dotenv import load_dotenv

load_dotenv()

MS_AZURE_ENDPOINT = os.getenv("MS_AZURE_ENDPOINT")
MS_AZURE_DEPLOYMENT_NAME = os.getenv("MS_AZURE_DEPLOYMENT_NAME")
MS_AZURE_SUBSCRIPTION_KEY = os.getenv("MS_AZURE_SUBSCRIPTION_KEY")
MS_AZURE_API_VERSION = os.getenv("MS_AZURE_API_VERSION")
RESUME_LINK = os.getenv("RESUME_LINK")
ALLOWED_ADMIN_IPS = { ip.strip() for ip in os.getenv("ALLOWED_ADMIN_IPS", "").split(",") if ip.strip() }
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN")