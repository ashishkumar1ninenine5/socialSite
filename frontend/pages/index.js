import { useEffect, useState } from 'react';
import { getMemes, likeMeme, unlikeMeme } from '../lib/api';

export default function Home() {
  const [memes, setMemes] = useState([]);
  const [userId, setUserId] = useState('');

  useEffect(() => {
    getMemes().then(setMemes).catch(() => setMemes([]));
  }, []);

  return (
    <div>
      <h1>Feed</h1>
      <div style={{ marginBottom: '1rem' }}>
        <input placeholder="Your user ID" value={userId} onChange={e => setUserId(e.target.value)} />
      </div>
      {memes.length === 0 && <p>No posts yet.</p>}
      {memes.map(m => (
        <div key={m.id} style={{ border: '1px solid #ccc', marginBottom: '1rem', padding: '1rem' }}>
          <p><strong>{m.author_id}</strong></p>
          <img src={m.media_url} alt={m.caption} style={{ maxWidth: '100%' }} />
          <p>{m.caption}</p>
          <p>{m.like_count || 0} likes</p>
          <button onClick={() => likeMeme(m.id, userId).then(getMemes).then(setMemes)}>Like</button>
          <button onClick={() => unlikeMeme(m.id, userId).then(getMemes).then(setMemes)}>Unlike</button>
        </div>
      ))}
    </div>
  );
}
