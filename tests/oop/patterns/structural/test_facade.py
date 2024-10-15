"""Test Facade DP"""

import unittest
from typing import Any
from unittest.mock import patch

from src.oop.patterns.structural.facade import VideoStreamingFacade


class TestVideoStreamingFacade(unittest.TestCase):
    """Test cases for the VideoStreamingFacade class."""

    @patch("builtins.print")
    def test_successful_watch_video(self, mock_print: Any) -> None:
        """Test the process of watching a video with successful authentication."""
        facade = VideoStreamingFacade()
        facade.watch_video("user", "password", "1234")

        # Check that the correct sequence of events is printed
        mock_print.assert_any_call("User 'user' authenticated successfully.")
        mock_print.assert_any_call("Loading preferences for user: user")
        mock_print.assert_any_call("Fetching recommendations for user: user")
        mock_print.assert_any_call("Playing video with ID: 1234")

    @patch("builtins.print")
    def test_failed_authentication(self, mock_print: Any) -> None:
        """Test the process of watching a video with failed authentication."""
        facade = VideoStreamingFacade()
        facade.watch_video("invalid_user", "wrong_password", "5678")

        # Check that authentication fails and no further steps are executed
        mock_print.assert_any_call("Authentication failed for user 'invalid_user'.")
        mock_print.assert_any_call("Unable to watch video. Authentication required.")

        # Check that loading preferences and playing video were not called
        self.assertNotIn(
            "Loading preferences for user: invalid_user", [call[0][0] for call in mock_print.call_args_list]
        )
        self.assertNotIn("Playing video with ID: 5678", [call[0][0] for call in mock_print.call_args_list])


if __name__ == "__main__":
    unittest.main()
