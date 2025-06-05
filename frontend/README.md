# Next.js Frontend

This folder contains a small Next.js application that works with the FastAPI backend.
Run the development server with:

```bash
npm install
npm run dev
```

The app provides basic Instagram‑style features:

- Sign up and sign in forms using the backend authentication endpoints
- A feed displaying memes from `/memes`
- Profile pages under `/profile/[id]`
- A simple form to upload new posts

Set the backend URL via the `NEXT_PUBLIC_API_URL` environment variable (defaults to `http://localhost:8080`).
