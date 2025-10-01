import json
from app.core.config import RESUME_LINK

def get_resume_link(version: str) -> str:
    resume_link = RESUME_LINK
    return json.dumps({
        "version": version,
        "resume_link": resume_link
    })