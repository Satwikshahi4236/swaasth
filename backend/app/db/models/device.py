from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..base import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    token = Column(String, unique=True, index=True, nullable=False)  # FCM token
    platform = Column(String, nullable=True)  # ios/android/web
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    user = relationship("User", backref="devices")