from fastapi import FastAPI
from .api.v1 import user

app = FastAPI(title="Meme Social Media API")
app.include_router(user.router)
