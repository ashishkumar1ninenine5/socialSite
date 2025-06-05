from typing import Optional


class UserRepository:
    def __init__(self, db):
        self.collection = db["users"]

    def get_by_email(self, email: str):
        return self.collection.find_one({"email": email})

    def create(self, email: str, hashed_password: str, full_name: Optional[str] = None):
        user = {"email": email, "hashed_password": hashed_password, "full_name": full_name}
        result = self.collection.insert_one(user)
        user["_id"] = result.inserted_id
        return user
