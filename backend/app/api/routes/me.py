from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ...security.auth import get_current_user_claims
from ...db.session import get_db
from ...db.models.user import User

router = APIRouter()

@router.get("/me")
def me(claims: dict = Depends(get_current_user_claims), db: Session = Depends(get_db)) -> dict:
    sub = claims.get("sub")
    if not sub:
        return {"anonymous": True}

    user = db.query(User).filter(User.sub == sub).first()
    if user is None:
        user = User(
            sub=sub,
            name=claims.get("name"),
            email=claims.get("email"),
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    return {
        "id": user.id,
        "sub": user.sub,
        "name": user.name,
        "email": user.email,
        "is_caregiver": user.is_caregiver,
    }