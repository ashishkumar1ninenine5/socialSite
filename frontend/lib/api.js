import axios from 'axios';

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8080',
});

export async function signup(email, password, full_name) {
  const res = await api.post('/users/signup', { email, password, full_name });
  return res.data;
}

export async function login(email, password) {
  const res = await api.post('/users/login', { email, password });
  return res.data;
}

export async function getMemes() {
  const res = await api.get('/memes');
  return res.data.memes;
}

export async function createMeme(author_id, caption, media_url) {
  const res = await api.post('/memes', { author_id, caption, media_url });
  return res.data;
}

export async function getProfile(id) {
  const res = await api.get(`/profile/${id}`);
  return res.data;
}

export async function likeMeme(id, user_id) {
  const res = await api.post(`/memes/${id}/like`, null, { params: { user_id } });
  return res.data;
}

export async function unlikeMeme(id, user_id) {
  const res = await api.delete(`/memes/${id}/like`, { params: { user_id } });
  return res.data;
}
