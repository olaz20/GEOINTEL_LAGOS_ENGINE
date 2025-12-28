import asyncio
from services.notications.channels.base import NotificationChannel
from core.database import AsyncSessionLocal
from services.user.user_repository import get_user_email
from tasks.email_tasks import send_email_task
from typing import Optional, Dict, Any


class EmailChannel(NotificationChannel):
    """
    Email notification channel.
    """

    def send(
        self,
        user_id: int,
        title: str,
        message: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """
        Sync entrypoint (called from service layer).
        """
        email = self._get_user_email_sync(user_id)

        if not email:
            return

        send_email_task.delay(
            subject=title,
            recipient_email=email,
            metadata={
                **(metadata or {}),
                "context": {
                    **(metadata.get("context", {}) if metadata else {}),
                    "message": message,
                },
            },
        )


    def _get_user_email_sync(self, user_id: int) -> str:
        """
        Safely bridge async DB call into sync code.
        """
        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            return asyncio.run_coroutine_threadsafe(
                self._fetch_email(user_id), loop
            ).result()

        return asyncio.run(self._fetch_email(user_id))

    async def _fetch_email(self, user_id: int) -> str:
        async with AsyncSessionLocal() as db:
            return await get_user_email(db, user_id)