from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from models.notification import Notification
from schemas.notifications import NotificationCreate
from .channels.inapp import InAppChannel
from .channels.email import EmailChannel
from .channels.push import PushChannel
import logging

CHANNEL_MAP = {
    "in_app": InAppChannel(),
    "email": EmailChannel(),
    "push": PushChannel(),
}

logger = logging.getLogger(__name__)
class NotificationService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def send_notification(self, data: NotificationCreate):
        if data.channel not in CHANNEL_MAP:
            raise HTTPException(status_code=400, detail="Invalid channel")

        notification = Notification(
            user_id=data.user_id,
            title=data.title,
            message=data.message,
            channel=data.channel,
            metadata=data.metadata,
        )

        self.db.add(notification)
        await self.db.commit()
        await self.db.refresh(notification)



        try :
            CHANNEL_MAP[data.channel].send(
                data.user_id,
                data.title,
                data.message,
                data.metadata,
            )
        except Exception as exc:
                logger.exception(
                    f"Notification failed via: {exc}"
                )

        return notification
