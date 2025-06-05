import { useState } from 'react';
import { createMeme } from '../lib/api';

export default function Upload() {
  const [authorId, setAuthorId] = useState('');
  const [caption, setCaption] = useState('');
  const [mediaUrl, setMediaUrl] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await createMeme(authorId, caption, mediaUrl);
      setMessage('Posted!');
      setCaption('');
      setMediaUrl('');
    } catch (err) {
      setMessage('Failed to post');
    }
  };

  return (
    <div>
      <h1>New Post</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <input placeholder="Your User ID" value={authorId} onChange={e => setAuthorId(e.target.value)} />
        </div>
        <div>
          <input placeholder="Caption" value={caption} onChange={e => setCaption(e.target.value)} />
        </div>
        <div>
          <input placeholder="Image URL" value={mediaUrl} onChange={e => setMediaUrl(e.target.value)} />
        </div>
        <button type="submit">Post</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}
