import json
from typing import Any

from app.external.resume import get_resume_link


def handle_tool_calls(response_message: Any, messages: list[dict[str, Any]]) -> None:
    if not response_message.tool_calls:
        return

    for tool_call in response_message.tool_calls:
        if tool_call.function.name != "get_resume":
            continue

        function_args = json.loads(tool_call.function.arguments)
        messages.append({
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": "get_resume",
            "content": get_resume_link(version=function_args.get("version")),
        })