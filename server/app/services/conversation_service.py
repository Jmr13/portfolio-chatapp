import os
import json
from typing import List, Dict
from openai import AzureOpenAI
from app.core.config import MS_AZURE_ENDPOINT, MS_AZURE_MODEL_NAME, MS_AZURE_DEPLOYMENT_NAME, MS_AZURE_SUBSCRIPTION_KEY, MS_AZURE_API_VERSION
from app.core.client import create_client
from app.core.tools import get_tools, handle_tool_calls

def run_conversation(messages: List[Dict]) -> Dict:
    client = create_client()
    tools = get_tools()

    response = client.chat.completions.create(
        model = MS_AZURE_DEPLOYMENT_NAME,
        messages = messages,
        tools = tools,
        tool_choice = "auto"
    )

    response_message = response.choices[0].message
    messages.append(response_message)

    handle_tool_calls(response_message, messages) 

    final_response = client.chat.completions.create(
        model = MS_AZURE_DEPLOYMENT_NAME,
        messages = messages,
    )

    return final_response.choices[0].message