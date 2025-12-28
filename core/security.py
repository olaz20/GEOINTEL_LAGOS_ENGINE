from datetime import datetime
import uuid
from core.config import settings
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User
from passlib.context import CryptContext
from sqlalchemy import select

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

async def initialize_default_admin(db: AsyncSession):
    admin_email = settings.default_admin_email
    result = await db.execute(select(User).where(User.email == admin_email))
    admin = result.scalar_one_or_none()
    if not admin:
        first_name = "Admin"
        last_name = "Admin"
        new_admin = User(
            id=uuid.uuid4(),  # Add if your model doesn't auto-generate
            email=admin_email,
            first_name=first_name,
            last_name=last_name,
            full_name=f"{first_name} {last_name}",
            password=hash_password(settings.admin_password),
            is_verified=True,
            is_admin=True,
            created_at=datetime.utcnow(),  # Add if not defaulted in model
            updated_at=datetime.utcnow(),
        )
        db.add(new_admin)
        await db.commit()
        await db.refresh(new_admin)
    return None