from sqlalchemy import Column, DateTime 
from datetime import datetime

class Audit:
    __abstract__ = True 

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)