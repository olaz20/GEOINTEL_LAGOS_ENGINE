from fastapi import HTTPException, status

from models.user import User
from schemas.auth import SignupRequest
from core.security import hash_password
from utils.tokens import build_verification_link, generate_email_verification_token
from utils.notification import notify_user
from sqlalchemy.ext.asyncio import AsyncSession

async def signup_user(db:  AsyncSession, data: SignupRequest) -> User:
    existing_user = db.query(User).filter(User.email == data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )
    
    verification_token = generate_email_verification_token()
    verification_link = build_verification_link(verification_token)
    user = User(
        first_name=data.first_name,
        last_name=data.last_name,
        full_name=f"{data.first_name} {data.last_name}",
        email=data.email,
        password=hash_password(data.password),
        is_verified=False,
        email_verification_token=verification_token,
    )
    
    
    db.add(user)
    await db.commit()
    await db.refresh(user)

    await notify_user(
        db=db,
        user_id=user.id,
        title="Verify your email address",
        message="Please verify your email address",
        channels=["email"],
        metadata={
            "template": "emails/verify_email.html",
            "text_template": "emails/verify_email.txt",
            "context": {
                "user": user,
                "verification_link": verification_link,
            },
        },
    )
    return user
