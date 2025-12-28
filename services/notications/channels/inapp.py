from .base import NotificationChannel


class InAppChannel(NotificationChannel):
    def send(self, user_id, title: str, message: str , metadata=None):
        return True
