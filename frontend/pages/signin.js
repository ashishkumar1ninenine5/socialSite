import { useState } from 'react';
import { login } from '../lib/api';

export default function SignIn() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await login(email, password);
      setMessage('Logged in!');
    } catch (err) {
      setMessage('Login failed');
    }
  };

  return (
    <div>
      <h1>Sign In</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
        </div>
        <div>
          <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
        </div>
        <button type="submit">Sign In</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}
