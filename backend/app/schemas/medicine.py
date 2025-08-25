from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date, time


class MedicineCreate(BaseModel):
    """Schema for creating medicine."""
    name: str
    description: Optional[str] = None
    dosage: str
    form: Optional[str] = None
    frequency: str
    duration_days: Optional[int] = None
    start_date: datetime
    end_date: Optional[datetime] = None
    instructions: Optional[str] = None
    prescribing_doctor: Optional[str] = None
    pharmacy: Optional[str] = None
    side_effects: Optional[str] = None


class MedicineUpdate(BaseModel):
    """Schema for updating medicine."""
    name: Optional[str] = None
    description: Optional[str] = None
    dosage: Optional[str] = None
    form: Optional[str] = None
    frequency: Optional[str] = None
    duration_days: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    instructions: Optional[str] = None
    prescribing_doctor: Optional[str] = None
    pharmacy: Optional[str] = None
    side_effects: Optional[str] = None
    is_active: Optional[bool] = None


class MedicineResponse(BaseModel):
    """Schema for medicine response."""
    id: int
    user_id: int
    name: str
    description: Optional[str] = None
    dosage: str
    form: Optional[str] = None
    frequency: str
    duration_days: Optional[int] = None
    start_date: datetime
    end_date: Optional[datetime] = None
    instructions: Optional[str] = None
    prescribing_doctor: Optional[str] = None
    pharmacy: Optional[str] = None
    refill_count: int
    side_effects: Optional[str] = None
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class MedicineReminderCreate(BaseModel):
    """Schema for creating medicine reminder."""
    medicine_id: int
    reminder_time: time
    days_of_week: Optional[str] = "1,2,3,4,5,6,7"


class MedicineReminderUpdate(BaseModel):
    """Schema for updating medicine reminder."""
    reminder_time: Optional[time] = None
    days_of_week: Optional[str] = None
    is_active: Optional[bool] = None


class MedicineReminderResponse(BaseModel):
    """Schema for medicine reminder response."""
    id: int
    user_id: int
    medicine_id: int
    reminder_time: time
    days_of_week: str
    is_active: bool
    notification_sent: bool
    last_notification_sent: Optional[datetime] = None
    snooze_count: int
    snooze_until: Optional[datetime] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class MedicineLogCreate(BaseModel):
    """Schema for creating medicine log."""
    medicine_id: int
    reminder_id: Optional[int] = None
    scheduled_time: datetime
    taken_time: Optional[datetime] = None
    status: str = "pending"
    dosage_taken: Optional[str] = None
    notes: Optional[str] = None
    side_effects_experienced: Optional[str] = None


class MedicineLogUpdate(BaseModel):
    """Schema for updating medicine log."""
    taken_time: Optional[datetime] = None
    status: Optional[str] = None
    dosage_taken: Optional[str] = None
    notes: Optional[str] = None
    side_effects_experienced: Optional[str] = None
    adherence_score: Optional[float] = None


class MedicineLogResponse(BaseModel):
    """Schema for medicine log response."""
    id: int
    user_id: int
    medicine_id: int
    reminder_id: Optional[int] = None
    scheduled_time: datetime
    taken_time: Optional[datetime] = None
    status: str
    dosage_taken: Optional[str] = None
    notes: Optional[str] = None
    side_effects_experienced: Optional[str] = None
    adherence_score: Optional[float] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True