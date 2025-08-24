import React from 'react';
import { Container, Typography, Grid, Paper, Box } from '@mui/material';

const DashboardPage: React.FC = () => {
  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom>
        Good Morning! 👋
      </Typography>
      <Typography variant="subtitle1" color="text.secondary" gutterBottom>
        Here's your health summary for today
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} sm={6} md={4}>
          <Paper sx={{ p: 2, textAlign: 'center' }}>
            <Typography variant="h6" color="text.secondary">
              Today's Medicines
            </Typography>
            <Typography variant="h4" color="primary">
              3 pending
            </Typography>
          </Paper>
        </Grid>
        
        <Grid item xs={12} sm={6} md={4}>
          <Paper sx={{ p: 2, textAlign: 'center' }}>
            <Typography variant="h6" color="text.secondary">
              Health Records
            </Typography>
            <Typography variant="h4" color="primary">
              2 new
            </Typography>
          </Paper>
        </Grid>
        
        <Grid item xs={12} sm={6} md={4}>
          <Paper sx={{ p: 2, textAlign: 'center' }}>
            <Typography variant="h6" color="text.secondary">
              Family Messages
            </Typography>
            <Typography variant="h4" color="primary">
              1 unread
            </Typography>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default DashboardPage;