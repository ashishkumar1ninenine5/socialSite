from ...domain.meme.repository import MemeRepository
from ...domain.like.repository import LikeRepository
from ...domain.comment.repository import CommentRepository
from ...domain.bookmark.repository import BookmarkRepository
from typing import Optional

class MemeService:
    def __init__(self, db):
        self.repo = MemeRepository(db)
        self.like_repo = LikeRepository(db)
        self.comment_repo = CommentRepository(db)
        self.bookmark_repo = BookmarkRepository(db)

    def create_meme(self, author_id: str, caption: str, hashtags: str, media_url: str):
        return self.repo.create(author_id, caption, hashtags, media_url)

    def list_memes(self):
        return self.repo.list_recent()

    def like(self, user_id: str, meme_id: str):
        self.like_repo.like(user_id, meme_id)
        count = self.like_repo.count_for_meme(meme_id)
        self.repo.collection.update_one({"_id": meme_id}, {"$set": {"like_count": count}})

    def unlike(self, user_id: str, meme_id: str):
        self.like_repo.unlike(user_id, meme_id)
        count = self.like_repo.count_for_meme(meme_id)
        self.repo.collection.update_one({"_id": meme_id}, {"$set": {"like_count": count}})

    def comment(self, user_id: str, meme_id: str, text: str, parent_id: Optional[str] = None):
        return self.comment_repo.add(user_id, meme_id, text, parent_id)

    def bookmark(self, user_id: str, meme_id: str):
        self.bookmark_repo.save(user_id, meme_id)

    def unbookmark(self, user_id: str, meme_id: str):
        self.bookmark_repo.unsave(user_id, meme_id)

    def trending(self):
        return list(self.repo.collection.find().sort("like_count", -1).limit(10))
