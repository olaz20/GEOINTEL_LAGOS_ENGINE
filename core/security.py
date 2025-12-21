from core.config import settings
from sqlalchemy.orm import Session
from models.user import User


def initialize_default_admin(db: Session):
    admin_email = settings.default_admin_email
    if not db.query(User).filter(User.email == admin_email).first():
        admin = User(
            email=admin_email,
            first_name ="Admin",
            last_name = "Admin",
            password=hash(settings.admin_password),
            is_verified=True,
            is_admin = True,
        )
        db.add(admin)
        db.commit()
        db.refresh(admin)
    return None
