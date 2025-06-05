class LikeRepository:
    def __init__(self, db):
        self.collection = db["likes"]

    def like(self, user_id: str, meme_id: str):
        self.collection.update_one(
            {"user_id": user_id, "meme_id": meme_id},
            {"$set": {"user_id": user_id, "meme_id": meme_id}},
            upsert=True,
        )

    def unlike(self, user_id: str, meme_id: str):
        self.collection.delete_one({"user_id": user_id, "meme_id": meme_id})

    def count_for_meme(self, meme_id: str) -> int:
        return self.collection.count_documents({"meme_id": meme_id})
