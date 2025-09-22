from config import settings
from openai import AzureOpenAI

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=settings.azure_endpoint,
    api_key=settings.api_key,
    api_version=settings.api_version
)

def get_model_response(messages: list, tools: list) -> dict:
    """Get the model's response."""
    response = client.chat.completions.create(
        model=settings.deployment_name,
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    return response.choices[0].message

def finalize_response(messages: list) -> str:
    """Get the final response from the model."""
    return client.chat.completions.create(
        model=settings.deployment_name,
        messages=messages,
    ).choices[0].message.content