from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from schemas.notifications import NotificationCreate, NotificationOut
from services.notications.service import NotificationService
from core.database import get_db

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.post("/", response_model=NotificationOut)
async def create_notification(
    payload: NotificationCreate,
    db: AsyncSession = Depends(get_db),
):
    service = NotificationService(db=db)
    return await service.send_notification(db, payload)
