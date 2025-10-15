import os
import json
from typing import List, Dict
from openai import AzureOpenAI
from app.external.index import get_resume_link
from app.core.config import MS_AZURE_ENDPOINT, MS_AZURE_MODEL_NAME, MS_AZURE_DEPLOYMENT_NAME, MS_AZURE_SUBSCRIPTION_KEY, MS_AZURE_API_VERSION

def run_conversation(messages: List[Dict]) -> Dict:
    client = AzureOpenAI(
        api_version = MS_AZURE_API_VERSION,
        azure_endpoint = MS_AZURE_ENDPOINT,
        api_key = MS_AZURE_SUBSCRIPTION_KEY,
    )
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_resume",
                "description": "Get the link of applicant's resume file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "version": {
                            "type": "string",
                            "description": "Version or type of resume (e.g. 'pdf', 'docx')",
                            "enum": ["pdf", "docx", "txt"]
                        }
                    },
                    "required": ["version"],
                },
            }
        }
    ]

    response = client.chat.completions.create(
        model = MS_AZURE_DEPLOYMENT_NAME,
        messages = messages,
        tools = tools,
        tool_choice = "auto"
    )

    response_message = response.choices[0].message
    messages.append(response_message)

    print("Model's response:")  
    print(response_message)

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

    final_response = client.chat.completions.create(
        model = MS_AZURE_DEPLOYMENT_NAME,
        messages = messages,
    )

    return final_response.choices[0].message