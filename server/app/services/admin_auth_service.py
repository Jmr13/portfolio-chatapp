from app.core.config import ADMIN_TOKEN, ALLOWED_ADMIN_IPS


def parse_admin_protocols(header_value: str) -> tuple[str, str] | None:
    protocols = [part.strip() for part in header_value.split(",") if part.strip()]
    if len(protocols) < 2:
        return None
    return protocols[0], protocols[1]


def is_authorized_admin(client_host: str, admin_token: str) -> bool:
    return client_host in ALLOWED_ADMIN_IPS and admin_token == ADMIN_TOKEN