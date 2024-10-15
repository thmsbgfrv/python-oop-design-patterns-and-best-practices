"""Module for Facade DP"""


class Authentication:
    """Handles user authentication."""

    def login(self, username: str, password: str) -> bool:
        """Simulates user login."""
        if username == "user" and password == "password":
            print(f"User '{username}' authenticated successfully.")
            return True

        print(f"Authentication failed for user '{username}'.")
        return False


class VideoPlayer:
    """Handles video playback."""

    def play_video(self, video_id: str) -> None:
        """Simulates playing a video."""
        print(f"Playing video with ID: {video_id}")


class Recommendations:
    """Handles video recommendations."""

    def get_recommendations(self, user_id: str) -> list[str]:
        """Simulates fetching recommendations for a user."""
        print(f"Fetching recommendations for user: {user_id}")
        return ["Video1", "Video2", "Video3"]


class UserPreferences:
    """Handles user preferences."""

    def load_preferences(self, user_id: str) -> dict[str, str]:
        """Simulates loading user preferences."""
        print(f"Loading preferences for user: {user_id}")
        return {"theme": "dark", "playback_speed": "1.5x"}


# Facade
class VideoStreamingFacade:
    """Facade that simplifies the interaction with the video streaming system."""

    def __init__(self) -> None:
        self.auth = Authentication()
        self.player = VideoPlayer()
        self.recommendations = Recommendations()
        self.preferences = UserPreferences()

    def watch_video(self, username: str, password: str, video_id: str) -> None:
        """Simplifies the process of watching a video."""
        if not self.auth.login(username, password):
            print("Unable to watch video. Authentication required.")
            return

        # Load user preferences and recommendations
        user_id = username
        self.preferences.load_preferences(user_id)
        self.recommendations.get_recommendations(user_id)

        # Play the video
        self.player.play_video(video_id)
