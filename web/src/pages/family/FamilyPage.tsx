import React from 'react';
import { Container, Typography } from '@mui/material';

const FamilyPage: React.FC = () => {
  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom>
        Family
      </Typography>
      <Typography variant="body1">
        Family communication and connections will be implemented here
      </Typography>
    </Container>
  );
};

export default FamilyPage;