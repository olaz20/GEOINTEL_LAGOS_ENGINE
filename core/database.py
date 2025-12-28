from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

Base = declarative_base()

from models.common import Audit
from models.user import User
from models.notification import Notification

SQLALCHEMY_DATABASE_URL = (
    f'postgresql+asyncpg://{settings.database_username}:{settings.database_password}'
    f'@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
)


engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)


AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)


async def get_db():
    async with AsyncSessionLocal() as db:
        yield db
