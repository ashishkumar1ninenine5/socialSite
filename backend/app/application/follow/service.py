from ...domain.follow.repository import FollowRepository

class FollowService:
    def __init__(self, db):
        self.repo = FollowRepository(db)

    def follow(self, follower_id: str, following_id: str):
        self.repo.follow(follower_id, following_id)

    def unfollow(self, follower_id: str, following_id: str):
        self.repo.unfollow(follower_id, following_id)

    def followers(self, user_id: str):
        return self.repo.followers(user_id)

    def following(self, user_id: str):
        return self.repo.following(user_id)
