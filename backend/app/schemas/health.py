from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date


class HealthRecordCreate(BaseModel):
    """Schema for creating health record."""
    record_type: str
    title: str
    description: Optional[str] = None
    diagnosis_code: Optional[str] = None
    provider_name: Optional[str] = None
    provider_contact: Optional[str] = None
    date_recorded: date
    follow_up_date: Optional[date] = None
    severity: Optional[str] = None
    status: Optional[str] = "active"
    attachments: Optional[str] = None
    notes: Optional[str] = None
    is_shared_with_family: Optional[bool] = False


class HealthRecordResponse(BaseModel):
    """Schema for health record response."""
    id: int
    user_id: int
    record_type: str
    title: str
    description: Optional[str] = None
    diagnosis_code: Optional[str] = None
    provider_name: Optional[str] = None
    provider_contact: Optional[str] = None
    date_recorded: date
    follow_up_date: Optional[date] = None
    severity: Optional[str] = None
    status: str
    attachments: Optional[str] = None
    notes: Optional[str] = None
    is_shared_with_family: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class VitalSignsCreate(BaseModel):
    """Schema for creating vital signs."""
    measurement_date: datetime
    systolic_bp: Optional[int] = None
    diastolic_bp: Optional[int] = None
    heart_rate: Optional[int] = None
    temperature: Optional[float] = None
    temperature_unit: Optional[str] = "C"
    weight: Optional[float] = None
    weight_unit: Optional[str] = "kg"
    height: Optional[float] = None
    height_unit: Optional[str] = "cm"
    bmi: Optional[float] = None
    blood_glucose: Optional[float] = None
    glucose_unit: Optional[str] = "mg/dL"
    glucose_time_relation: Optional[str] = None
    oxygen_saturation: Optional[float] = None
    respiratory_rate: Optional[int] = None
    blood_pressure_medication_taken: Optional[bool] = False
    measurement_method: Optional[str] = None
    device_name: Optional[str] = None
    notes: Optional[str] = None


class VitalSignsResponse(BaseModel):
    """Schema for vital signs response."""
    id: int
    user_id: int
    measurement_date: datetime
    systolic_bp: Optional[int] = None
    diastolic_bp: Optional[int] = None
    heart_rate: Optional[int] = None
    temperature: Optional[float] = None
    temperature_unit: str
    weight: Optional[float] = None
    weight_unit: str
    height: Optional[float] = None
    height_unit: str
    bmi: Optional[float] = None
    blood_glucose: Optional[float] = None
    glucose_unit: str
    glucose_time_relation: Optional[str] = None
    oxygen_saturation: Optional[float] = None
    respiratory_rate: Optional[int] = None
    blood_pressure_medication_taken: bool
    measurement_method: Optional[str] = None
    device_name: Optional[str] = None
    notes: Optional[str] = None
    is_flagged: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True