import * as Notifications from 'expo-notifications';
import * as Device from 'expo-device';
import { Platform } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';

export interface MedicineReminder {
  id: string;
  medicineName: string;
  dosage: string;
  time: string;
  days: number[]; // 0-6 (Sunday-Saturday)
  isActive: boolean;
}

class NotificationServiceClass {
  async requestPermissions(): Promise<boolean> {
    if (!Device.isDevice) {
      console.log('Push notifications only work on physical devices');
      return false;
    }

    const { status: existingStatus } = await Notifications.getPermissionsAsync();
    let finalStatus = existingStatus;

    if (existingStatus !== 'granted') {
      const { status } = await Notifications.requestPermissionsAsync();
      finalStatus = status;
    }

    if (finalStatus !== 'granted') {
      console.log('Failed to get push token for push notification');
      return false;
    }

    return true;
  }

  async getExpoPushToken(): Promise<string | null> {
    try {
      const token = (await Notifications.getExpoPushTokenAsync()).data;
      console.log('Expo Push Token:', token);
      
      // Store token locally
      await AsyncStorage.setItem('expo_push_token', token);
      
      return token;
    } catch (error) {
      console.error('Error getting Expo push token:', error);
      return null;
    }
  }

  async scheduleMedicineReminder(reminder: MedicineReminder): Promise<string | null> {
    try {
      const trigger = {
        hour: parseInt(reminder.time.split(':')[0]),
        minute: parseInt(reminder.time.split(':')[1]),
        repeats: true,
      };

      const notificationId = await Notifications.scheduleNotificationAsync({
        content: {
          title: 'Medicine Reminder 💊',
          body: `Time to take your ${reminder.medicineName} (${reminder.dosage})`,
          sound: 'default',
          data: {
            reminderType: 'medicine',
            medicineId: reminder.id,
            medicineName: reminder.medicineName,
          },
        },
        trigger,
      });

      console.log(`Scheduled medicine reminder: ${notificationId}`);
      return notificationId;
    } catch (error) {
      console.error('Error scheduling medicine reminder:', error);
      return null;
    }
  }

  async scheduleMedicineReminders(): Promise<void> {
    try {
      // Get medicine reminders from storage or API
      const remindersJson = await AsyncStorage.getItem('medicine_reminders');
      if (!remindersJson) return;

      const reminders: MedicineReminder[] = JSON.parse(remindersJson);
      
      // Cancel existing scheduled notifications
      await Notifications.cancelAllScheduledNotificationsAsync();

      // Schedule new notifications
      for (const reminder of reminders) {
        if (reminder.isActive) {
          await this.scheduleMedicineReminder(reminder);
        }
      }
    } catch (error) {
      console.error('Error scheduling medicine reminders:', error);
    }
  }

  async cancelMedicineReminder(notificationId: string): Promise<void> {
    try {
      await Notifications.cancelScheduledNotificationAsync(notificationId);
      console.log(`Cancelled medicine reminder: ${notificationId}`);
    } catch (error) {
      console.error('Error cancelling medicine reminder:', error);
    }
  }

  async sendImmediateNotification(title: string, body: string, data?: any): Promise<string | null> {
    try {
      const notificationId = await Notifications.scheduleNotificationAsync({
        content: {
          title,
          body,
          sound: 'default',
          data,
        },
        trigger: null, // Send immediately
      });

      return notificationId;
    } catch (error) {
      console.error('Error sending immediate notification:', error);
      return null;
    }
  }

  async handleNotificationReceived(notification: Notifications.Notification): Promise<void> {
    console.log('Notification received:', notification);
    
    const data = notification.request.content.data;
    
    if (data?.reminderType === 'medicine') {
      // Handle medicine reminder notification
      console.log(`Medicine reminder for: ${data.medicineName}`);
    }
  }

  async handleNotificationResponse(response: Notifications.NotificationResponse): Promise<void> {
    console.log('Notification response:', response);
    
    const data = response.notification.request.content.data;
    
    if (data?.reminderType === 'medicine') {
      // Navigate to medicine screen or show confirmation dialog
      console.log(`User tapped medicine reminder for: ${data.medicineName}`);
    }
  }

  setupNotificationListeners(): void {
    // Listener for notifications received while app is running
    Notifications.addNotificationReceivedListener(this.handleNotificationReceived);

    // Listener for when user taps on notification
    Notifications.addNotificationResponseReceivedListener(this.handleNotificationResponse);
  }

  async getAllScheduledNotifications(): Promise<Notifications.NotificationRequest[]> {
    try {
      return await Notifications.getAllScheduledNotificationsAsync();
    } catch (error) {
      console.error('Error getting scheduled notifications:', error);
      return [];
    }
  }

  async testNotification(): Promise<void> {
    await this.sendImmediateNotification(
      'Test Notification',
      'This is a test notification from Swaasth Elder Health app!'
    );
  }
}

export const NotificationService = new NotificationServiceClass();