import json
from typing import List
from services.openai_service import get_model_response, finalize_response
from models.time_utils import get_current_time

def process_tool_call(tool_call) -> dict:
    """Process the tool call from model and return updated messages."""
    if tool_call.function.name == "get_current_time":
        function_args = json.loads(tool_call.function.arguments)
        time_response = get_current_time(location=function_args.get("location"))
        return {
            "tool_call_id": tool_call.id,
            "role": "tool",
            "name": "get_current_time",
            "content": time_response,
        }
    return {}

def handle_tool_calls(response_message) -> List[dict]:
    """Handle any tool calls from the model response and return updated messages."""
    tool_calls = response_message.tool_calls or []
    return list(filter(None, map(process_tool_call, tool_calls)))

def run_conversation(messages: List[dict]) -> str:
    """Handle the entire conversation flow."""
    tools = [{
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the current time in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name, e.g. San Francisco",
                    },
                },
                "required": ["location"],
            },
        }
    }]
    
    response_message = get_model_response(messages, tools)
    messages.append(response_message)
    
    updated_messages = handle_tool_calls(response_message)
    messages.extend(updated_messages)
    
    return finalize_response(messages)