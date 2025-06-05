# Meme Social Media Platform

This repository contains a basic skeleton for a meme-based social media platform built using **FastAPI** for the backend and **Next.js** for the frontend. It follows a simplified Domain‑Driven Design (DDD) folder layout to help organize the project.

## Folder structure
```
backend/
  app/
    api/          - FastAPI routers
    application/  - Business logic services
    domain/       - ORM models and repositories
    infrastructure/ - Database setup
    main.py       - FastAPI application entrypoint
frontend/         - (placeholder for Next.js app)
```

## Backend
Install dependencies and run the API server:
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000` with automatic Swagger docs at `/docs`.

## Frontend
A minimal Next.js app can be added under `frontend/`. You can generate one with `npx create-next-app` or integrate an existing frontend later.

This skeleton only includes a simple user signup and login endpoint as a starting point for implementing the rest of the features described in the project overview.
