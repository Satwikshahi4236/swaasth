import React from 'react';
import { View, StyleSheet } from 'react-native';
import { Title, Text } from 'react-native-paper';

const ProfileScreen: React.FC = () => {
  return (
    <View style={styles.container}>
      <Title>Profile</Title>
      <Text>User profile and settings</Text>
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

export default ProfileScreen;