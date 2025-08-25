import React from 'react';
import { View, StyleSheet } from 'react-native';
import { Title, Text } from 'react-native-paper';

const FamilyScreen: React.FC = () => {
  return (
    <View style={styles.container}>
      <Title>Family</Title>
      <Text>Family communication and connections</Text>
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

export default FamilyScreen;