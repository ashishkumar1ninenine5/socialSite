class BookmarkRepository:
    def __init__(self, db):
        self.collection = db["bookmarks"]

    def save(self, user_id: str, meme_id: str):
        self.collection.update_one(
            {"user_id": user_id, "meme_id": meme_id},
            {"$set": {"user_id": user_id, "meme_id": meme_id}},
            upsert=True,
        )

    def unsave(self, user_id: str, meme_id: str):
        self.collection.delete_one({"user_id": user_id, "meme_id": meme_id})
