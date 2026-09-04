import json

from app.core.config import RESUME_LINK


def get_resume_link(version: str) -> str:
    return json.dumps({
        "version": version,
        "resume_link": RESUME_LINK,
    })