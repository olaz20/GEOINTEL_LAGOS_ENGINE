from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import get_db
from schemas.auth import SignupRequest, SignupResponse
from services.auth import signup_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup", response_model=SignupResponse)
async def signup(payload: SignupRequest, db: AsyncSession = Depends(get_db)):
    user =  await signup_user(db, payload)
    return SignupResponse(
        id=str(user.id),
        email=user.email,
        full_name=user.full_name
    )
