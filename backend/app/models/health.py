from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class HealthRecord(Base):
    """Health record model for storing medical history and health data."""
    __tablename__ = "health_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    record_type = Column(String(50), nullable=False)  # diagnosis, test_result, appointment, surgery, etc.
    title = Column(String(200), nullable=False)
    description = Column(Text)
    diagnosis_code = Column(String(20))  # ICD-10 code
    provider_name = Column(String(200))
    provider_contact = Column(String(200))
    date_recorded = Column(Date, nullable=False)
    follow_up_date = Column(Date)
    severity = Column(String(20))  # mild, moderate, severe, critical
    status = Column(String(20), default="active")  # active, resolved, chronic, monitoring
    attachments = Column(Text)  # JSON string for file URLs
    notes = Column(Text)
    is_shared_with_family = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="health_records")


class VitalSigns(Base):
    """Vital signs model for tracking health measurements."""
    __tablename__ = "vital_signs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    measurement_date = Column(DateTime(timezone=True), nullable=False)
    
    # Blood pressure
    systolic_bp = Column(Integer)  # mmHg
    diastolic_bp = Column(Integer)  # mmHg
    
    # Heart rate
    heart_rate = Column(Integer)  # bpm
    
    # Temperature
    temperature = Column(Float)  # Celsius
    temperature_unit = Column(String(1), default="C")  # C or F
    
    # Weight and BMI
    weight = Column(Float)  # kg
    weight_unit = Column(String(2), default="kg")  # kg or lb
    height = Column(Float)  # cm
    height_unit = Column(String(2), default="cm")  # cm or in
    bmi = Column(Float)
    
    # Blood glucose
    blood_glucose = Column(Float)  # mg/dL
    glucose_unit = Column(String(5), default="mg/dL")  # mg/dL or mmol/L
    glucose_time_relation = Column(String(20))  # fasting, before_meal, after_meal, bedtime
    
    # Oxygen saturation
    oxygen_saturation = Column(Float)  # percentage
    
    # Other measurements
    respiratory_rate = Column(Integer)  # breaths per minute
    blood_pressure_medication_taken = Column(Boolean, default=False)
    
    # Metadata
    measurement_method = Column(String(50))  # manual, device, estimated
    device_name = Column(String(100))
    notes = Column(Text)
    is_flagged = Column(Boolean, default=False)  # flagged for abnormal values
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="vital_signs")