"""Module for Decorator"""


class Notification:
    """Base class for notifications."""

    def send(self) -> None:
        """Send the notification."""
        print("Sending notification...")


class EmailNotification(Notification):
    """Decorator class to add email notification capability."""

    def __init__(self, notification: Notification) -> None:
        self._notification = notification

    def send(self) -> None:
        """Send the email notification."""
        self._notification.send()  # Call the original notification
        self.send_email()

    def send_email(self) -> None:
        """Send email notification."""
        print("Sending email notification...")


class SMSNotification(Notification):
    """Decorator class to add SMS notification capability."""

    def __init__(self, notification: Notification) -> None:
        self._notification = notification

    def send(self) -> None:
        """Send the SMS notification."""
        self._notification.send()  # Call the original notification
        self.send_sms()

    def send_sms(self) -> None:
        """Send SMS notification."""
        print("Sending SMS notification...")
