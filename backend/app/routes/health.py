from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.health import HealthRecord, VitalSigns

router = APIRouter()


@router.get("/records")
async def get_health_records(db: Session = Depends(get_db)):
    """Get health records."""
    return {"message": "Get health records endpoint"}


@router.post("/records")
async def create_health_record(db: Session = Depends(get_db)):
    """Create health record."""
    return {"message": "Create health record endpoint"}


@router.get("/vitals")
async def get_vital_signs(db: Session = Depends(get_db)):
    """Get vital signs."""
    return {"message": "Get vital signs endpoint"}


@router.post("/vitals")
async def create_vital_signs(db: Session = Depends(get_db)):
    """Create vital signs record."""
    return {"message": "Create vital signs endpoint"}