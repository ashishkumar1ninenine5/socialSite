from fastapi import FastAPI
from .api.v1 import user, profile, follow, meme, search, admin
import os
import uvicorn

app = FastAPI(title="Meme Social Media API")
app.include_router(user.router)
app.include_router(profile.router)
app.include_router(follow.router)
app.include_router(meme.router)
app.include_router(search.router)
app.include_router(admin.router)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
