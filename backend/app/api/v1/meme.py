from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from ...infrastructure.database import get_db
from ...application.meme.service import MemeService

router = APIRouter(prefix="/memes", tags=["memes"])

def get_database():
    return get_db()

class MemeCreate(BaseModel):
    author_id: str
    caption: str
    media_url: str
    hashtags: str = ""


@router.post("/")
def create_meme(meme: MemeCreate, db = Depends(get_database)):
    service = MemeService(db)
    created = service.create_meme(meme.author_id, meme.caption, meme.hashtags, meme.media_url)
    return {"id": str(created["_id"])}

@router.get("/")
def list_memes(db = Depends(get_database)):
    service = MemeService(db)
    memes = service.list_memes()
    return {"memes": [{**m, "id": str(m["_id"])} for m in memes]}

@router.post("/{meme_id}/like")
def like_meme(meme_id: str, user_id: str, db = Depends(get_database)):
    service = MemeService(db)
    service.like(user_id, meme_id)
    return {"message": "liked"}

@router.delete("/{meme_id}/like")
def unlike_meme(meme_id: str, user_id: str, db = Depends(get_database)):
    service = MemeService(db)
    service.unlike(user_id, meme_id)
    return {"message": "unliked"}

@router.post("/{meme_id}/comment")
def comment_meme(meme_id: str, user_id: str, text: str, parent_id: Optional[str] = None, db = Depends(get_database)):
    service = MemeService(db)
    comment = service.comment(user_id, meme_id, text, parent_id)
    return {"id": str(comment["_id"])}

@router.post("/{meme_id}/bookmark")
def bookmark_meme(meme_id: str, user_id: str, db = Depends(get_database)):
    service = MemeService(db)
    service.bookmark(user_id, meme_id)
    return {"message": "bookmarked"}

@router.delete("/{meme_id}/bookmark")
def unbookmark_meme(meme_id: str, user_id: str, db = Depends(get_database)):
    service = MemeService(db)
    service.unbookmark(user_id, meme_id)
    return {"message": "unbookmarked"}

@router.get("/trending")
def trending_memes(db = Depends(get_database)):
    service = MemeService(db)
    memes = service.trending()
    return {"memes": [{**m, "id": str(m["_id"])} for m in memes]}
