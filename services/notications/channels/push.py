from .base import NotificationChannel


class PushChannel(NotificationChannel):
    def send(self, user_id, title: str, message: str):
        print(f"PUSH → {user_id}: {title}")
