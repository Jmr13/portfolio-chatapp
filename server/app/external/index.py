import json
from app.core.config import MS_AZURE_ENDPOINT

def get_resume_link(version: str) -> str:
    resume_link = MS_AZURE_ENDPOINT
    return json.dumps({
        "version": version,
        "resume_link": resume_link
    })