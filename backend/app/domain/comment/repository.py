from typing import Optional


class CommentRepository:
    def __init__(self, db):
        self.collection = db["comments"]

    def add(self, user_id: str, meme_id: str, text: str, parent_id: Optional[str] = None):
        comment = {"user_id": user_id, "meme_id": meme_id, "text": text, "parent_id": parent_id}
        res = self.collection.insert_one(comment)
        comment["_id"] = res.inserted_id
        return comment

    def list_for_meme(self, meme_id: str):
        return list(self.collection.find({"meme_id": meme_id}))
