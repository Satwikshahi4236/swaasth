from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class User(Base):
    """User model for authentication and basic user information."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    role = Column(String(50), default="elder")  # elder, caregiver, family_member
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    profile = relationship("UserProfile", back_populates="user", uselist=False)
    medicines = relationship("Medicine", back_populates="user")
    medicine_reminders = relationship("MedicineReminder", back_populates="user")
    medicine_logs = relationship("MedicineLog", back_populates="user")
    health_records = relationship("HealthRecord", back_populates="user")
    vital_signs = relationship("VitalSigns", back_populates="user")
    
    # Family connections
    family_connections_as_elder = relationship(
        "FamilyConnection", 
        foreign_keys="FamilyConnection.elder_id",
        back_populates="elder"
    )
    family_connections_as_caregiver = relationship(
        "FamilyConnection", 
        foreign_keys="FamilyConnection.caregiver_id",
        back_populates="caregiver"
    )
    
    # Messages
    sent_messages = relationship(
        "FamilyMessage",
        foreign_keys="FamilyMessage.sender_id",
        back_populates="sender"
    )
    received_messages = relationship(
        "FamilyMessage",
        foreign_keys="FamilyMessage.receiver_id", 
        back_populates="receiver"
    )


class UserProfile(Base):
    """Extended user profile information."""
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    phone_number = Column(String(20))
    date_of_birth = Column(Date)
    emergency_contact_name = Column(String(200))
    emergency_contact_phone = Column(String(20))
    medical_conditions = Column(Text)  # JSON string for medical conditions
    allergies = Column(Text)  # JSON string for allergies
    profile_picture_url = Column(String(500))
    address = Column(Text)
    city = Column(String(100))
    state = Column(String(100))
    zip_code = Column(String(20))
    country = Column(String(100))
    timezone = Column(String(50), default="UTC")
    preferred_language = Column(String(10), default="en")
    
    # Notification preferences
    notifications_enabled = Column(Boolean, default=True)
    email_notifications = Column(Boolean, default=True)
    push_notifications = Column(Boolean, default=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    user = relationship("User", back_populates="profile")