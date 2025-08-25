import React from 'react';
import { Container, Typography } from '@mui/material';

const ProfilePage: React.FC = () => {
  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom>
        Profile
      </Typography>
      <Typography variant="body1">
        User profile and settings will be implemented here
      </Typography>
    </Container>
  );
};

export default ProfilePage;