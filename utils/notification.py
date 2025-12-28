from schemas.notifications import NotificationCreate
from sqlalchemy.ext.asyncio import AsyncSession
import logging
from typing import List, Optional, Dict, Any
logger = logging.getLogger(__name__)
from services.notications.service import NotificationService

async def notify_user(
        db: AsyncSession,
        user_id: int,
        title: str,
        message: str,
        channel: str = "in_app",
        metadata: Optional[Dict[str, Any]] = None,
) -> None:
    try:
        data = NotificationCreate(
            user_id=user_id,
            title=title,
            message=message,
            channel=channel,
            metadata=metadata,
        )
        await NotificationService(db).send_notification(
        data
        )
        logger.info(
            f"Notification sent successfully to user {user_id} via {channel}"
        )
    except Exception as exc:
        logger.exception(
            f"Failed to send notification to user {user_id}: {exc}"
        )
        raise