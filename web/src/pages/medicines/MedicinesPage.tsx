import React from 'react';
import { Container, Typography } from '@mui/material';

const MedicinesPage: React.FC = () => {
  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom>
        Medicines
      </Typography>
      <Typography variant="body1">
        Medicine management and reminders will be implemented here
      </Typography>
    </Container>
  );
};

export default MedicinesPage;