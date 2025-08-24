from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.medicine import Medicine, MedicineReminder, MedicineLog

router = APIRouter()


@router.get("/")
async def get_medicines(db: Session = Depends(get_db)):
    """Get user's medicines."""
    return {"message": "Get medicines endpoint"}


@router.post("/")
async def create_medicine(db: Session = Depends(get_db)):
    """Create a new medicine."""
    return {"message": "Create medicine endpoint"}


@router.get("/reminders")
async def get_medicine_reminders(db: Session = Depends(get_db)):
    """Get medicine reminders."""
    return {"message": "Get medicine reminders endpoint"}


@router.post("/reminders")
async def create_medicine_reminder(db: Session = Depends(get_db)):
    """Create medicine reminder."""
    return {"message": "Create medicine reminder endpoint"}


@router.post("/log")
async def log_medicine_taken(db: Session = Depends(get_db)):
    """Log that medicine was taken."""
    return {"message": "Log medicine taken endpoint"}