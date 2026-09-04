from typing import Any


def get_tools() -> list[dict[str, Any]]:
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