import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const RegisterPage: React.FC = () => {
  return (
    <Container maxWidth="sm">
      <Box sx={{ mt: 8, textAlign: 'center' }}>
        <Typography variant="h4">Register</Typography>
        <Typography variant="body1" sx={{ mt: 2 }}>
          User registration functionality will be implemented here
        </Typography>
      </Box>
    </Container>
  );
};

export default RegisterPage;