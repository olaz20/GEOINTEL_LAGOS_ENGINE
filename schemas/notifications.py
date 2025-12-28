from pydantic import BaseModel
from typing import Literal, Optional, Dict, Any
from uuid import UUID


class NotificationCreate(BaseModel):
    user_id: UUID
    title: str
    message: str
    channel: Literal["in_app", "email", "push"]
    metadata: Optional[Dict[str, Any]] = None


class NotificationOut(BaseModel):
    id: UUID
    title: str
    message: str
    channel: str
    is_read: bool
