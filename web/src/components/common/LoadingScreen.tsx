import React from 'react';
import { Box, CircularProgress, Typography } from '@mui/material';

const LoadingScreen: React.FC = () => {
  return (
    <Box
      display="flex"
      flexDirection="column"
      justifyContent="center"
      alignItems="center"
      minHeight="100vh"
      bgcolor="primary.main"
      color="white"
    >
      <Typography variant="h3" component="h1" gutterBottom fontWeight={300}>
        Swaasth Elder Health
      </Typography>
      <CircularProgress color="inherit" size={40} />
    </Box>
  );
};

export default LoadingScreen;