import Link from 'next/link';
import { useRouter } from 'next/router';

export default function Layout({ children }) {
  const router = useRouter();

  return (
    <div style={{ fontFamily: 'Arial, sans-serif' }}>
      <nav style={{ padding: '1rem', borderBottom: '1px solid #ccc' }}>
        <Link href="/" style={{ marginRight: '1rem' }}>Feed</Link>
        <Link href="/upload" style={{ marginRight: '1rem' }}>New Post</Link>
        <Link href="/signup" style={{ marginRight: '1rem' }}>Sign Up</Link>
        <Link href="/signin" style={{ marginRight: '1rem' }}>Sign In</Link>
      </nav>
      <main style={{ padding: '1rem' }}>{children}</main>
    </div>
  );
}
