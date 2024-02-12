from django.test import TestCase
from django.utils import timezone
from hello.models import LogMessage
import datetime

class LogMessageModelTest(TestCase):

    def create_logmessage(self, message="Test Log Message"):
        """
        ARRANGE
        Create and return a LogMessage instance.
        """
        return LogMessage.objects.create(
            message=message,
            log_date=timezone.now()
        )

    def test_logmessage_creation(self):
        """
        ACT
        Test the creation of the LogMessage instance.
        """
        log_message = self.create_logmessage()
        """
        ASSERT
        Confirm log_message is an instance of LogMessage.
        """
        self.assertTrue(isinstance(log_message, LogMessage))

    def test_logmessage_data(self):
        """
        ACT
        Test the creation of the LogMessage message.
        """
        log_message = self.create_logmessage()
        date = timezone.localtime(log_message.log_date)
        """
        ASSERT
        Confirm message is formatted correctly and as expected.
        """
        expected_message = f"'{ log_message.message }' logged on {date.strftime('%A, %d %B, %Y at %X')}"
        self.assertEqual(str(log_message), expected_message)
