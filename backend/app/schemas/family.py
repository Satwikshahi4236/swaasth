from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class FamilyConnectionCreate(BaseModel):
    """Schema for creating family connection."""
    elder_id: int
    caregiver_id: int
    relationship_type: str
    permissions: Optional[str] = None
    is_primary_caregiver: Optional[bool] = False
    emergency_contact: Optional[bool] = False


class FamilyConnectionResponse(BaseModel):
    """Schema for family connection response."""
    id: int
    elder_id: int
    caregiver_id: int
    relationship_type: str
    status: str
    permissions: Optional[str] = None
    is_primary_caregiver: bool
    emergency_contact: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class FamilyMessageCreate(BaseModel):
    """Schema for creating family message."""
    receiver_id: int
    subject: Optional[str] = None
    content: str
    message_type: Optional[str] = "general"
    priority: Optional[str] = "normal"
    reply_to_message_id: Optional[int] = None


class FamilyMessageResponse(BaseModel):
    """Schema for family message response."""
    id: int
    sender_id: int
    receiver_id: int
    subject: Optional[str] = None
    content: str
    message_type: str
    priority: str
    is_read: bool
    is_encrypted: bool
    read_at: Optional[datetime] = None
    reply_to_message_id: Optional[int] = None
    attachment_url: Optional[str] = None
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True