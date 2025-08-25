from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.family import FamilyConnection, FamilyMessage

router = APIRouter()


@router.get("/connections")
async def get_family_connections(db: Session = Depends(get_db)):
    """Get family connections."""
    return {"message": "Get family connections endpoint"}


@router.post("/connections")
async def create_family_connection(db: Session = Depends(get_db)):
    """Create family connection."""
    return {"message": "Create family connection endpoint"}


@router.get("/messages")
async def get_family_messages(db: Session = Depends(get_db)):
    """Get family messages."""
    return {"message": "Get family messages endpoint"}


@router.post("/messages")
async def send_family_message(db: Session = Depends(get_db)):
    """Send family message."""
    return {"message": "Send family message endpoint"}