from datetime import datetime

class MemeRepository:
    def __init__(self, db):
        self.collection = db["memes"]

    def create(self, author_id: str, caption: str, hashtags: str, media_url: str):
        meme = {
            "author_id": author_id,
            "caption": caption,
            "hashtags": hashtags,
            "media_url": media_url,
            "created_at": datetime.utcnow(),
            "like_count": 0,
        }
        res = self.collection.insert_one(meme)
        meme["_id"] = res.inserted_id
        return meme

    def list_recent(self):
        return list(self.collection.find().sort("created_at", -1))

    def get(self, meme_id: str):
        return self.collection.find_one({"_id": meme_id})
