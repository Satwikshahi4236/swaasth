from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime
from sqlalchemy.orm import relationship
from ..base import Base

class Reminder(Base):
    __tablename__ = "reminders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    medicine_id = Column(Integer, ForeignKey("medicines.id"), nullable=True)
    schedule = Column(String, nullable=False)  # cron or human readable spec
    enabled = Column(Boolean, default=True)
    next_at = Column(DateTime, nullable=True)

    user = relationship("User", backref="reminders")
    medicine = relationship("Medicine", backref="reminders")