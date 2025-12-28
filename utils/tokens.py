import secrets
from core.config import settings

def generate_email_verification_token() -> str:
    return secrets.token_urlsafe(32)

def build_verification_link(token: str) -> str:
    return f"{settings.FRONTEND_URL}/verify-email?token={token}"