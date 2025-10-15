import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()

MS_AZURE_ENDPOINT = os.getenv("MS_AZURE_ENDPOINT")
MS_AZURE_MODEL_NAME = os.getenv("MS_AZURE_MODEL_NAME")
MS_AZURE_DEPLOYMENT_NAME = os.getenv("MS_AZURE_DEPLOYMENT_NAME")
MS_AZURE_SUBSCRIPTION_KEY = os.getenv("MS_AZURE_SUBSCRIPTION_KEY")
MS_AZURE_API_VERSION = os.getenv("MS_AZURE_API_VERSION")
RESUME_LINK = os.getenv("RESUME_LINK")