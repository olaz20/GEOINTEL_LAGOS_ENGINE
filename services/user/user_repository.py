from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User

async def get_user_email(db: AsyncSession, user_id: int) -> str:
    result = await db.execute(
        select(User.email).where(User.id == user_id)
    )
    email = result.scalar_one_or_none()

    if not email:
        raise ValueError("User not found")

    return email
