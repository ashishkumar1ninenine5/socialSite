import { useEffect, useState } from 'react';
import { getMemes } from '../lib/api';

export default function Home() {
  const [memes, setMemes] = useState([]);

  useEffect(() => {
    getMemes().then(setMemes).catch(() => setMemes([]));
  }, []);

  return (
    <div>
      <h1>Feed</h1>
      {memes.length === 0 && <p>No posts yet.</p>}
      {memes.map(m => (
        <div key={m.id} style={{ border: '1px solid #ccc', marginBottom: '1rem', padding: '1rem' }}>
          <p><strong>{m.author_id}</strong></p>
          <img src={m.media_url} alt={m.caption} style={{ maxWidth: '100%' }} />
          <p>{m.caption}</p>
        </div>
      ))}
    </div>
  );
}
