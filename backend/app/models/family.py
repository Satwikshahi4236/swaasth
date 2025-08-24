from sqlalchemy import Column, Integer, String, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database import Base


class FamilyConnection(Base):
    """Family connection model for linking elders with caregivers/family members."""
    __tablename__ = "family_connections"

    id = Column(Integer, primary_key=True, index=True)
    elder_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    caregiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    relationship_type = Column(String(50), nullable=False)  # family, caregiver, doctor, etc.
    status = Column(String(20), default="pending")  # pending, accepted, rejected, blocked
    permissions = Column(Text)  # JSON string for permissions (view_medications, receive_alerts, etc.)
    is_primary_caregiver = Column(Boolean, default=False)
    emergency_contact = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    elder = relationship("User", foreign_keys=[elder_id], back_populates="family_connections_as_elder")
    caregiver = relationship("User", foreign_keys=[caregiver_id], back_populates="family_connections_as_caregiver")


class FamilyMessage(Base):
    """Family message model for secure communication between family members."""
    __tablename__ = "family_messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    subject = Column(String(200))
    content = Column(Text, nullable=False)
    message_type = Column(String(50), default="general")  # general, emergency, medication_alert, health_update
    priority = Column(String(20), default="normal")  # low, normal, high, urgent
    is_read = Column(Boolean, default=False)
    is_encrypted = Column(Boolean, default=True)
    read_at = Column(DateTime(timezone=True))
    reply_to_message_id = Column(Integer, ForeignKey("family_messages.id"))
    attachment_url = Column(String(500))  # URL to attachment file
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    sender = relationship("User", foreign_keys=[sender_id], back_populates="sent_messages")
    receiver = relationship("User", foreign_keys=[receiver_id], back_populates="received_messages")
    reply_to = relationship("FamilyMessage", remote_side=[id])