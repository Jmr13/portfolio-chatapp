import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    azure_endpoint: str = os.getenv("MS_AZURE_OPENAI_ENDPOINT")
    api_key: str = os.getenv("MS_AZURE_AI_API_KEY")
    api_version: str = os.getenv("MS_AZURE_OPENAI_MODEL_APIV")
    deployment_name: str = os.getenv("MS_AZURE_OPENAI_MODEL_NAME")
    
settings = Settings()