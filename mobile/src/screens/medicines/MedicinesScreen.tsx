import React from 'react';
import { View, StyleSheet } from 'react-native';
import { Title, Text } from 'react-native-paper';

const MedicinesScreen: React.FC = () => {
  return (
    <View style={styles.container}>
      <Title>Medicines</Title>
      <Text>Medicine management and reminders</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
});

export default MedicinesScreen;