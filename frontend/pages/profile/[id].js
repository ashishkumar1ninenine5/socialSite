import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';
import { getProfile } from '../../lib/api';

export default function Profile() {
  const router = useRouter();
  const { id } = router.query;
  const [profile, setProfile] = useState(null);

  useEffect(() => {
    if (id) {
      getProfile(id).then(setProfile).catch(() => setProfile(null));
    }
  }, [id]);

  if (!profile) return <p>Loading...</p>;

  return (
    <div>
      <h1>{profile.full_name || profile.email}</h1>
      {profile.avatar && (
        <img src={profile.avatar} alt="avatar" style={{ width: '200px' }} />
      )}
      <p>{profile.bio}</p>
    </div>
  );
}
