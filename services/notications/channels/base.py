from abc import ABC, abstractmethod
from typing import Optional, Dict, Any

class NotificationChannel(ABC):
    @abstractmethod
    def send(self, user_id, title: str, message: str,  metadata: Optional[Dict[str, Any]] = None,):
        pass
