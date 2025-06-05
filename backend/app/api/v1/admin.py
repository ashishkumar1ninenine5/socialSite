from fastapi import APIRouter, Depends
from ...infrastructure.database import get_db

router = APIRouter(prefix="/admin", tags=["admin"])

def get_database():
    return get_db()

@router.get("/users")
def list_users(db = Depends(get_database)):
    users = list(db["users"].find())
    return {"users": [{**u, "id": str(u["_id"])} for u in users]}

@router.get("/memes")
def list_memes(db = Depends(get_database)):
    memes = list(db["memes"].find())
    return {"memes": [{**m, "id": str(m["_id"])} for m in memes]}
