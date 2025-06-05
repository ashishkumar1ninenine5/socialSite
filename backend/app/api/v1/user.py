from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...infrastructure.database import SessionLocal, Base, engine
from ...application.user.service import UserService
from ...domain.user import models

Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(email: str, password: str, full_name: str | None = None, db: Session = Depends(get_db)):
    service = UserService(db)
    existing = service.repo.get_by_email(email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = service.create_user(email, password, full_name)
    return {"id": user.id, "email": user.email, "full_name": user.full_name}

@router.post("/login")
def login(email: str, password: str, db: Session = Depends(get_db)):
    service = UserService(db)
    user = service.authenticate_user(email, password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Logged in", "user_id": user.id}
