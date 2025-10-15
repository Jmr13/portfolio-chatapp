import json
from typing import List, Dict, Any
from app.external.index import get_resume_link

def get_tools() -> List[Dict[str, Any]]:
    return [
        {
            "type": "function",
            "function": {
                "name": "get_resume",
                "description": "Get the link of applicant's resume file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "version": {"type": "string", "enum": ["pdf", "docx", "txt"]}
                    },
                    "required": ["version"],
                },
            },
        }
    ]

def handle_tool_calls(response_message, messages: List[Dict]):
    if response_message.tool_calls:
        for tool_call in response_message.tool_calls:
            if tool_call.function.name == "get_resume":
                function_args = json.loads(tool_call.function.arguments)
                file_response = get_resume_link(
                    version=function_args.get("version")
                )
                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": "get_resume",
                    "content": file_response,
                })
    else:
        print("No tool calls were made by the model.") 