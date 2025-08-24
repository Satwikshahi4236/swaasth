from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Float, Time
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class Medicine(Base):
    """Medicine model for storing medication information."""
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String(200), nullable=False)
    description = Column(Text)
    dosage = Column(String(100), nullable=False)  # e.g., "10mg", "2 tablets"
    form = Column(String(50))  # tablet, liquid, injection, etc.
    frequency = Column(String(100), nullable=False)  # daily, twice daily, weekly, etc.
    duration_days = Column(Integer)  # treatment duration in days
    start_date = Column(DateTime(timezone=True), nullable=False)
    end_date = Column(DateTime(timezone=True))
    instructions = Column(Text)  # special instructions
    prescribing_doctor = Column(String(200))
    pharmacy = Column(String(200))
    refill_count = Column(Integer, default=0)
    side_effects = Column(Text)  # JSON string for side effects
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="medicines")
    reminders = relationship("MedicineReminder", back_populates="medicine")
    logs = relationship("MedicineLog", back_populates="medicine")


class MedicineReminder(Base):
    """Medicine reminder model for scheduling medication alerts."""
    __tablename__ = "medicine_reminders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    medicine_id = Column(Integer, ForeignKey("medicines.id"), nullable=False)
    reminder_time = Column(Time, nullable=False)  # time of day for reminder
    days_of_week = Column(String(20), default="1,2,3,4,5,6,7")  # comma-separated days (1=Monday)
    is_active = Column(Boolean, default=True)
    notification_sent = Column(Boolean, default=False)
    last_notification_sent = Column(DateTime(timezone=True))
    snooze_count = Column(Integer, default=0)
    snooze_until = Column(DateTime(timezone=True))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="medicine_reminders")
    medicine = relationship("Medicine", back_populates="reminders")


class MedicineLog(Base):
    """Medicine log model for tracking medication intake."""
    __tablename__ = "medicine_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    medicine_id = Column(Integer, ForeignKey("medicines.id"), nullable=False)
    reminder_id = Column(Integer, ForeignKey("medicine_reminders.id"))
    scheduled_time = Column(DateTime(timezone=True), nullable=False)
    taken_time = Column(DateTime(timezone=True))
    status = Column(String(20), default="pending")  # pending, taken, missed, skipped
    dosage_taken = Column(String(100))  # actual dosage taken
    notes = Column(Text)  # user notes about the medication
    side_effects_experienced = Column(Text)  # JSON string for side effects
    adherence_score = Column(Float)  # calculated adherence score
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="medicine_logs")
    medicine = relationship("Medicine", back_populates="logs")