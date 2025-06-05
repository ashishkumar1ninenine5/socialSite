from fastapi import APIRouter, Depends
from ...infrastructure.database import get_db
from ...application.follow.service import FollowService

router = APIRouter(prefix="/follow", tags=["follow"])

def get_database():
    return get_db()

@router.post("/{user_id}/follow/{target_id}")
def follow_user(user_id: str, target_id: str, db = Depends(get_database)):
    service = FollowService(db)
    service.follow(user_id, target_id)
    return {"message": "followed"}

@router.delete("/{user_id}/follow/{target_id}")
def unfollow_user(user_id: str, target_id: str, db = Depends(get_database)):
    service = FollowService(db)
    service.unfollow(user_id, target_id)
    return {"message": "unfollowed"}

@router.get("/{user_id}/followers")
def get_followers(user_id: str, db = Depends(get_database)):
    service = FollowService(db)
    return {"followers": service.followers(user_id)}

@router.get("/{user_id}/following")
def get_following(user_id: str, db = Depends(get_database)):
    service = FollowService(db)
    return {"following": service.following(user_id)}
