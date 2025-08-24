import React from 'react';
import { Container, Typography } from '@mui/material';

const HealthPage: React.FC = () => {
  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom>
        Health Records
      </Typography>
      <Typography variant="body1">
        Health records and vital signs will be implemented here
      </Typography>
    </Container>
  );
};

export default HealthPage;