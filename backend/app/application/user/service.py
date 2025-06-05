from passlib.context import CryptContext
from sqlalchemy.orm import Session
from ...domain.user.repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, email: str, password: str, full_name: str | None = None):
        hashed_password = pwd_context.hash(password)
        return self.repo.create(email=email, hashed_password=hashed_password, full_name=full_name)

    def authenticate_user(self, email: str, password: str):
        user = self.repo.get_by_email(email)
        if not user:
            return None
        if not pwd_context.verify(password, user.hashed_password):
            return None
        return user
