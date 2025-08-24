from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..database import get_db
from ..models.user import User, UserProfile

router = APIRouter()


@router.get("/profile")
async def get_user_profile(db: Session = Depends(get_db)):
    """Get user profile information."""
    return {"message": "User profile endpoint"}


@router.put("/profile")
async def update_user_profile(db: Session = Depends(get_db)):
    """Update user profile information.""" 
    return {"message": "Update user profile endpoint"}


@router.post("/fcm-token")
async def register_fcm_token(db: Session = Depends(get_db)):
    """Register FCM token for push notifications."""
    return {"message": "FCM token registration endpoint"}