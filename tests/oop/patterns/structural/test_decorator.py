"""Decorator test"""
import unittest
from typing import Any
from unittest.mock import patch

from oop.patterns.structural.decorator import EmailNotification, Notification, SMSNotification


class TestNotificationDecorator(unittest.TestCase):
    """Test cases for Notification and its Decorators."""

    @patch('builtins.print')
    def test_plain_notification(self, mock_print: Any) -> None:
        """Test plain notification sending."""
        notification = Notification()
        notification.send()
        mock_print.assert_any_call("Sending notification...")

    @patch('builtins.print')
    def test_email_notification(self, mock_print: Any) -> None:
        """Test notification sending with email."""
        notification = EmailNotification(Notification())
        notification.send()
        mock_print.assert_any_call("Sending notification...")
        mock_print.assert_any_call("Sending email notification...")

    @patch('builtins.print')
    def test_sms_notification(self, mock_print: Any) -> None:
        """Test notification sending with SMS."""
        notification = SMSNotification(Notification())
        notification.send()
        mock_print.assert_any_call("Sending notification...")
        mock_print.assert_any_call("Sending SMS notification...")

    @patch('builtins.print')
    def test_email_and_sms_notification(self, mock_print: Any) -> None:
        """Test notification sending with both email and SMS."""
        notification = EmailNotification(Notification())
        sms_notification = SMSNotification(notification)
        sms_notification.send()
        mock_print.assert_any_call("Sending notification...")
        mock_print.assert_any_call("Sending email notification...")
        mock_print.assert_any_call("Sending SMS notification...")
