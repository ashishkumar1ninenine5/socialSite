from ...domain.meme.repository import MemeRepository

class SearchService:
    def __init__(self, db):
        self.repo = MemeRepository(db)

    def search(self, query: str):
        q = {
            "$or": [
                {"caption": {"$regex": query, "$options": "i"}},
                {"hashtags": {"$regex": query, "$options": "i"}},
            ]
        }
        return list(self.repo.collection.find(q))
