import uuid
from datetime import datetime
from sqlalchemy import Column, String, Boolean, DateTime,  JSON
from sqlalchemy.dialects.postgresql import UUID

from core.database import Base
from models.common import Audit

class Notification(Base, Audit):
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), nullable=False)

    title = Column(String, nullable=False)
    message = Column(String, nullable=False)

    channel = Column(String, nullable=False)  
    is_read = Column(Boolean, default=False)
    data_metadata = Column(JSON, nullable=True)

