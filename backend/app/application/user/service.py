from passlib.context import CryptContext
from typing import Optional
from ...domain.user.repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db):
        self.repo = UserRepository(db)

    def create_user(self, email: str, password: str, full_name: Optional[str] = None):
        hashed_password = pwd_context.hash(password)
        return self.repo.create(email=email, hashed_password=hashed_password, full_name=full_name)

    def authenticate_user(self, email: str, password: str):
        user = self.repo.get_by_email(email)
        if not user:
            return None
        if not pwd_context.verify(password, user["hashed_password"]):
            return None
        return user
