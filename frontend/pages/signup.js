import { useState } from 'react';
import { signup } from '../lib/api';

export default function SignUp() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [fullName, setFullName] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      await signup(email, password, fullName);
      setMessage('Account created!');
    } catch (err) {
      setMessage('Signup failed');
    }
  };

  return (
    <div>
      <h1>Sign Up</h1>
      <form onSubmit={handleSubmit}>
        <div>
          <input placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
        </div>
        <div>
          <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
        </div>
        <div>
          <input placeholder="Full Name" value={fullName} onChange={e => setFullName(e.target.value)} />
        </div>
        <button type="submit">Sign Up</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}
