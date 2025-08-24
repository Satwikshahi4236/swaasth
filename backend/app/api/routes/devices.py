from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...security.auth import get_current_user_claims
from ...db.session import get_db
from ...db.models.device import Device

router = APIRouter()

@router.post("/register", response_model=dict)
def register_device(payload: dict, claims: dict = Depends(get_current_user_claims), db: Session = Depends(get_db)):
    user_id = _get_user_id(claims, db)
    token = payload.get("token")
    platform = payload.get("platform")
    if not token:
        return {"ok": False, "error": "token required"}

    device = db.query(Device).filter(Device.token == token).first()
    if device is None:
        device = Device(user_id=user_id, token=token, platform=platform)
        db.add(device)
        db.commit()
        db.refresh(device)
    else:
        device.user_id = user_id
        device.platform = platform
        db.commit()

    return {"ok": True}


def _get_user_id(claims: dict, db: Session) -> int:
    from ...db.models.user import User
    sub = claims.get("sub")
    user = db.query(User).filter(User.sub == sub).first()
    if user is None:
        raise Exception("User not found")
    return user.id