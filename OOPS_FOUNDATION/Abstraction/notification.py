from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")
    
class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")
    
class PopUpNotification(Notification):
    def send(self, message):
        print(f"Sending PopUp Notification: {message}")

# Polymorphic function

def send_notification(notification: Notification, message):
    notification.send(message=message)

send_notification(SMSNotification(), message="User logged in...")