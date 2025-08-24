from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ...security.auth import get_current_user_claims
from ...db.session import get_db
from ...db.models.medicine import Medicine
from ...db.models.reminder import Reminder

router = APIRouter()

@router.get("/", response_model=List[dict])
def list_medicines(claims: dict = Depends(get_current_user_claims), db: Session = Depends(get_db)):
    user_id = _get_user_id(claims, db)
    meds = db.query(Medicine).filter(Medicine.user_id == user_id).all()
    return [_serialize_medicine(m) for m in meds]

@router.post("/", response_model=dict)
def create_medicine(payload: dict, claims: dict = Depends(get_current_user_claims), db: Session = Depends(get_db)):
    user_id = _get_user_id(claims, db)
    med = Medicine(user_id=user_id, name=payload.get("name"), dosage=payload.get("dosage"), instructions=payload.get("instructions"))
    db.add(med)
    db.commit()
    db.refresh(med)
    return _serialize_medicine(med)

@router.delete("/{medicine_id}")
def delete_medicine(medicine_id: int, claims: dict = Depends(get_current_user_claims), db: Session = Depends(get_db)):
    user_id = _get_user_id(claims, db)
    med = db.query(Medicine).filter(Medicine.id == medicine_id, Medicine.user_id == user_id).first()
    if med is None:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(med)
    db.commit()
    return {"ok": True}

@router.post("/{medicine_id}/reminders", response_model=dict)
def create_reminder(medicine_id: int, payload: dict, claims: dict = Depends(get_current_user_claims), db: Session = Depends(get_db)):
    user_id = _get_user_id(claims, db)
    med = db.query(Medicine).filter(Medicine.id == medicine_id, Medicine.user_id == user_id).first()
    if med is None:
        raise HTTPException(status_code=404, detail="Medicine not found")
    reminder = Reminder(user_id=user_id, medicine_id=medicine_id, schedule=payload.get("schedule", ""))
    db.add(reminder)
    db.commit()
    db.refresh(reminder)
    return _serialize_reminder(reminder)


def _get_user_id(claims: dict, db: Session) -> int:
    from ...db.models.user import User
    sub = claims.get("sub")
    user = db.query(User).filter(User.sub == sub).first()
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user.id


def _serialize_medicine(m: Medicine) -> dict:
    return {
        "id": m.id,
        "name": m.name,
        "dosage": m.dosage,
        "instructions": m.instructions,
    }


def _serialize_reminder(r: Reminder) -> dict:
    return {
        "id": r.id,
        "schedule": r.schedule,
        "enabled": r.enabled,
        "medicine_id": r.medicine_id,
    }