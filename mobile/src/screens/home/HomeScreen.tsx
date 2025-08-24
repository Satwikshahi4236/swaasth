import React from 'react';
import { View, StyleSheet, ScrollView } from 'react-native';
import { Title, Card, Text, Button } from 'react-native-paper';
import { SafeAreaView } from 'react-native-safe-area-context';
import { Ionicons } from '@expo/vector-icons';

const HomeScreen: React.FC = () => {
  return (
    <SafeAreaView style={styles.container}>
      <ScrollView style={styles.scrollView}>
        <View style={styles.header}>
          <Title style={styles.title}>Good Morning! 👋</Title>
          <Text style={styles.subtitle}>Here's your health summary for today</Text>
        </View>

        <View style={styles.cardsContainer}>
          <Card style={styles.card}>
            <Card.Content>
              <Text style={styles.cardTitle}>Today's Medicines</Text>
              <Text style={styles.cardValue}>3 pending</Text>
            </Card.Content>
          </Card>

          <Card style={styles.card}>
            <Card.Content>
              <Text style={styles.cardTitle}>Health Records</Text>
              <Text style={styles.cardValue}>2 new</Text>
            </Card.Content>
          </Card>

          <Card style={styles.card}>
            <Card.Content>
              <Text style={styles.cardTitle}>Family Messages</Text>
              <Text style={styles.cardValue}>1 unread</Text>
            </Card.Content>
          </Card>
        </View>

        <Button mode="contained" style={styles.button}>
          Quick Medicine Log
        </Button>
      </ScrollView>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  scrollView: {
    flex: 1,
  },
  header: {
    padding: 16,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    marginTop: 4,
  },
  cardsContainer: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    padding: 8,
    justifyContent: 'space-between',
  },
  card: {
    width: '48%',
    marginBottom: 16,
    marginHorizontal: '1%',
  },
  cardTitle: {
    fontSize: 14,
    color: '#666',
    marginBottom: 8,
  },
  cardValue: {
    fontSize: 20,
    fontWeight: 'bold',
  },
  button: {
    margin: 16,
  },
});

export default HomeScreen;