import React from 'react';
import { View, StyleSheet } from 'react-native';
import { Title, Text } from 'react-native-paper';

const HealthScreen: React.FC = () => {
  return (
    <View style={styles.container}>
      <Title>Health</Title>
      <Text>Health records and vital signs</Text>
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

export default HealthScreen;