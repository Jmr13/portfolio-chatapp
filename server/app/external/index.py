import json
from app.core.config import Credential

def get_resume_link(version: str) -> str:
    resume_link = Credential.AZURE_ENDPOINT
    return json.dumps({
        "version": version,
        "resume_link": resume_link
    })