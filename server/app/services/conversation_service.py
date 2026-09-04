from typing import Any

from app.core.azure_client import create_client
from app.core.config import MS_AZURE_DEPLOYMENT_NAME
from app.core.tool_executor import handle_tool_calls
from app.core.tool_registry import get_tools


def run_conversation(messages: list[dict[str, Any]]) -> Any:
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