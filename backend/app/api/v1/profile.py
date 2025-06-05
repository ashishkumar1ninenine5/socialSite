from fastapi import APIRouter, Depends, HTTPException
from ...infrastructure.database import get_db
from ...application.user.service import UserService

router = APIRouter(prefix="/profile", tags=["profile"])

def get_database():
    return get_db()

@router.get("/{user_id}")
def get_profile(user_id: str, db = Depends(get_database)):
    service = UserService(db)
    user = service.repo.collection.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": str(user["_id"]),
        "email": user["email"],
        "full_name": user.get("full_name"),
        "bio": user.get("bio"),
        "avatar": user.get("avatar"),
    }

@router.put("/{user_id}")
def update_profile(user_id: str, bio: str | None = None, avatar: str | None = None, db = Depends(get_database)):
    service = UserService(db)
    update = {}
    if bio is not None:
        update["bio"] = bio
    if avatar is not None:
        update["avatar"] = avatar
    if update:
        service.repo.collection.update_one({"_id": user_id}, {"$set": update})
    user = service.repo.collection.find_one({"_id": user_id})
    return {
        "id": str(user["_id"]),
        "bio": user.get("bio"),
        "avatar": user.get("avatar"),
    }
