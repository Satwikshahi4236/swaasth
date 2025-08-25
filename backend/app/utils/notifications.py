import firebase_admin
from firebase_admin import credentials, messaging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional, List, Dict, Any
import json
import logging
import time
from ..config import settings

logger = logging.getLogger(__name__)

# Initialize Firebase Admin SDK (if credentials are provided)
firebase_app = None
if all([
    settings.firebase_project_id,
    settings.firebase_private_key,
    settings.firebase_client_email
]):
    try:
        cred_dict = {
            "type": "service_account",
            "project_id": settings.firebase_project_id,
            "private_key_id": settings.firebase_private_key_id,
            "private_key": settings.firebase_private_key.replace('\\n', '\n'),
            "client_email": settings.firebase_client_email,
            "client_id": settings.firebase_client_id,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": settings.firebase_client_x509_cert_url
        }
        
        cred = credentials.Certificate(cred_dict)
        firebase_app = firebase_admin.initialize_app(cred)
        logger.info("Firebase Admin SDK initialized successfully")
    except Exception as e:
        logger.error(f"Failed to initialize Firebase Admin SDK: {e}")


async def send_push_notification(
    token: str,
    title: str,
    body: str,
    data: Optional[Dict[str, str]] = None,
    notification_type: str = "general"
) -> bool:
    """
    Send a push notification using Firebase Cloud Messaging.
    
    Args:
        token: FCM registration token
        title: Notification title
        body: Notification body
        data: Additional data payload
        notification_type: Type of notification
        
    Returns:
        bool: True if successful, False otherwise
    """
    if not firebase_app:
        logger.warning("Firebase not initialized. Cannot send push notification.")
        return False
    
    try:
        # Create the notification
        notification = messaging.Notification(
            title=title,
            body=body
        )
        
        # Add custom data
        notification_data = data or {}
        notification_data.update({
            "type": notification_type,
            "timestamp": str(int(time.time()))
        })
        
        # Create the message
        message = messaging.Message(
            notification=notification,
            data=notification_data,
            token=token,
            android=messaging.AndroidConfig(
                notification=messaging.AndroidNotification(
                    icon="ic_notification",
                    color="#2196F3",
                    sound="default"
                ),
                priority="high"
            ),
            apns=messaging.APNSConfig(
                payload=messaging.APNSPayload(
                    aps=messaging.Aps(
                        alert=messaging.ApsAlert(
                            title=title,
                            body=body
                        ),
                        sound="default",
                        badge=1
                    )
                )
            )
        )
        
        # Send the message
        response = messaging.send(message)
        logger.info(f"Push notification sent successfully. Message ID: {response}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send push notification: {e}")
        return False


async def send_bulk_push_notifications(
    tokens: List[str],
    title: str,
    body: str,
    data: Optional[Dict[str, str]] = None,
    notification_type: str = "general"
) -> Dict[str, Any]:
    """
    Send push notifications to multiple devices.
    
    Args:
        tokens: List of FCM registration tokens
        title: Notification title
        body: Notification body
        data: Additional data payload
        notification_type: Type of notification
        
    Returns:
        dict: Results with success/failure counts
    """
    if not firebase_app:
        logger.warning("Firebase not initialized. Cannot send bulk push notifications.")
        return {"success_count": 0, "failure_count": len(tokens)}
    
    try:
        # Create the notification
        notification = messaging.Notification(
            title=title,
            body=body
        )
        
        # Add custom data
        notification_data = data or {}
        notification_data.update({
            "type": notification_type,
            "timestamp": str(int(time.time()))
        })
        
        # Create multicast message
        message = messaging.MulticastMessage(
            notification=notification,
            data=notification_data,
            tokens=tokens,
            android=messaging.AndroidConfig(
                notification=messaging.AndroidNotification(
                    icon="ic_notification",
                    color="#2196F3",
                    sound="default"
                ),
                priority="high"
            ),
            apns=messaging.APNSConfig(
                payload=messaging.APNSPayload(
                    aps=messaging.Aps(
                        alert=messaging.ApsAlert(
                            title=title,
                            body=body
                        ),
                        sound="default",
                        badge=1
                    )
                )
            )
        )
        
        # Send the message
        response = messaging.send_multicast(message)
        
        logger.info(f"Bulk push notifications sent. Success: {response.success_count}, Failure: {response.failure_count}")
        
        return {
            "success_count": response.success_count,
            "failure_count": response.failure_count,
            "responses": response.responses
        }
        
    except Exception as e:
        logger.error(f"Failed to send bulk push notifications: {e}")
        return {"success_count": 0, "failure_count": len(tokens)}


async def send_email_notification(
    to_email: str,
    subject: str,
    body: str,
    is_html: bool = False
) -> bool:
    """
    Send an email notification.
    
    Args:
        to_email: Recipient email address
        subject: Email subject
        body: Email body
        is_html: Whether body is HTML
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # For demo purposes, we'll just log the email
        # In production, you would configure SMTP settings
        logger.info(f"Email notification sent to {to_email}: {subject}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send email notification: {e}")
        return False


def create_medicine_reminder_notification(
    medicine_name: str,
    dosage: str,
    user_name: str
) -> Dict[str, str]:
    """
    Create a standardized medicine reminder notification.
    
    Args:
        medicine_name: Name of the medicine
        dosage: Dosage information
        user_name: User's name
        
    Returns:
        dict: Notification title and body
    """
    return {
        "title": "Medicine Reminder",
        "body": f"Hi {user_name}, it's time to take your {medicine_name} ({dosage})",
        "data": {
            "medicine_name": medicine_name,
            "dosage": dosage,
            "action": "take_medicine"
        }
    }


def create_emergency_notification(
    user_name: str,
    emergency_type: str,
    details: str
) -> Dict[str, str]:
    """
    Create an emergency notification.
    
    Args:
        user_name: User's name
        emergency_type: Type of emergency
        details: Emergency details
        
    Returns:
        dict: Notification title and body
    """
    return {
        "title": f"Emergency Alert - {user_name}",
        "body": f"{emergency_type}: {details}",
        "data": {
            "emergency_type": emergency_type,
            "user_name": user_name,
            "action": "emergency_alert"
        }
    }