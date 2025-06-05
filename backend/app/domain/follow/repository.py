class FollowRepository:
    def __init__(self, db):
        self.collection = db["follows"]

    def follow(self, follower_id: str, following_id: str):
        self.collection.update_one(
            {"follower_id": follower_id, "following_id": following_id},
            {"$set": {"follower_id": follower_id, "following_id": following_id}},
            upsert=True,
        )

    def unfollow(self, follower_id: str, following_id: str):
        self.collection.delete_one({"follower_id": follower_id, "following_id": following_id})

    def followers(self, user_id: str):
        return list(self.collection.find({"following_id": user_id}))

    def following(self, user_id: str):
        return list(self.collection.find({"follower_id": user_id}))
