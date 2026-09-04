from openai import AzureOpenAI

from app.core.config import (
    MS_AZURE_API_VERSION,
    MS_AZURE_ENDPOINT,
    MS_AZURE_SUBSCRIPTION_KEY,
)


def create_client() -> AzureOpenAI:
    return AzureOpenAI(
        api_version=MS_AZURE_API_VERSION,
        azure_endpoint=MS_AZURE_ENDPOINT,
        api_key=MS_AZURE_SUBSCRIPTION_KEY,
    )