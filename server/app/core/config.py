import os
from dotenv import load_dotenv

load_dotenv()

AZURE_ENDPOINT = os.getenv("MS_AZURE_OPENAI_ENDPOINT")
API_KEY = os.getenv("MS_AZURE_AI_API_KEY")
API_VERSION = os.getenv("MS_AZURE_OPENAI_MODEL_APIV")
DEPLOYMENT_NAME = os.getenv("MS_AZURE_OPENAI_MODEL_NAME")
RESUME_LINK = os.getenv("RESUME_LINK")