# Meme Social Media Platform

This repository contains a basic skeleton for a meme-based social media platform built using **FastAPI** for the backend and **Next.js** for the frontend. It follows a simplified Domain‑Driven Design (DDD) folder layout to help organize the project.

## Folder structure
```
backend/
  app/
    api/          - FastAPI routers
    application/  - Business logic services
    domain/       - Pydantic models and repositories
    infrastructure/ - MongoDB setup
    main.py       - FastAPI application entrypoint
frontend/         - Next.js app
```

## Backend
Install dependencies and run the API server (requires a running MongoDB instance). The server port can be changed via the `PORT` environment variable (default `8080`):
```bash
cd backend
pip install -r requirements.txt
python -m app.main
```
The API will be available at `http://localhost:8080` (or your chosen `PORT`) with automatic Swagger docs at `/docs`.

## Frontend
A minimal Next.js app lives under `frontend/`. Install dependencies and start the dev server:
```bash
cd frontend
npm install
npm run dev
```

The backend now exposes additional endpoints for profiles, following, meme posting and engagement (likes, comments and bookmarks) as well as a simple search and admin interface.
