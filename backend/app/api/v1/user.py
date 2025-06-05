from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from ...infrastructure.database import get_db
from ...application.user.service import UserService

router = APIRouter(prefix="/users", tags=["users"])

def get_database():
    return get_db()

@router.post("/signup")
def signup(email: str, password: str, full_name: Optional[str] = None, db = Depends(get_database)):
    service = UserService(db)
    existing = service.repo.get_by_email(email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = service.create_user(email, password, full_name)
    return {"id": str(user["_id"]), "email": user["email"], "full_name": user.get("full_name")}

@router.post("/login")
def login(email: str, password: str, db = Depends(get_database)):
    service = UserService(db)
    user = service.authenticate_user(email, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Logged in", "user_id": str(user["_id"])}
