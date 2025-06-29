from abc import ABC, abstractmethod
from enum import Enum, auto
from datetime import datetime
import re

# =========================
# Part 1: Data Type Design
# =========================

class UserProfile:
    """
    Represents a user's profile containing personal details and preferences.
    """
    def __init__(self, name: str, age: int, preferences: dict, is_premium: bool):
        assert isinstance(name, str), "Name must be a string"
        assert isinstance(age, int) and age >= 0, "Age must be a non-negative integer"
        assert isinstance(preferences, dict), "Preferences must be a dictionary"
        assert isinstance(is_premium, bool), "is_premium must be a boolean"
        self.name = name
        self.age = age
        self.preferences = preferences
        self.is_premium = is_premium

class CommandType(Enum):
    """
    Supported command categories for the AI assistant.
    """
    UNKNOWN = auto()
    RECOMMEND_MUSIC = auto()
    SUGGEST_WORKOUT = auto()
    SCHEDULE_STUDY = auto()

# Keyword-based intent parser
def parse_intent(input_str: str) -> CommandType:
    """
    Infers command type from input text using regex matching.
    """
    text = input_str.lower()
    if re.search(r"\b(music|song|play)\b", text):
        return CommandType.RECOMMEND_MUSIC
    if re.search(r"\b(workout|exercise|train)\b", text):
        return CommandType.SUGGEST_WORKOUT
    if re.search(r"\b(study|schedule|learn)\b", text):
        return CommandType.SCHEDULE_STUDY
    return CommandType.UNKNOWN

class Request:
    """
    Encapsulates a user's request: raw text, timestamp, and inferred command type.
    """
    def __init__(self, input_str: str, timestamp: datetime, command: CommandType = None):
        assert isinstance(input_str, str) and input_str.strip(), "Input string required"
        assert isinstance(timestamp, datetime), "Timestamp must be datetime"
        command = command or parse_intent(input_str)
        assert isinstance(command, CommandType), "Invalid command type"
        self.input = input_str
        self.timestamp = timestamp
        self.command_type = command

class Response:
    """
    Response structure: message, confidence score, and action performed flag.
    """
    def __init__(self, message: str, confidence: float, action_performed: bool):
        assert isinstance(message, str), "Message must be a string"
        assert isinstance(confidence, float) and 0.0 <= confidence <= 1.0, "Confidence must be between 0 and 1"
        assert isinstance(action_performed, bool), "action_performed must be boolean"
        self.message = message
        self.confidence = confidence
        self.action_performed = action_performed

# ==================================
# Part 2: Core OOP Assistant Classes
# ==================================

class AIAssistant(ABC):
    """
    Interface for AI assistant variants (greeting + request handling).
    """
    def __init__(self, profile: UserProfile):
        self.profile = profile

    def greet_user(self) -> Response:
        """
        Returns a personalized greeting response.
        """
        greeting = f"Hello, {self.profile.name}! How can assistance begin today?"
        return Response(greeting, confidence=1.0, action_performed=False)

    @abstractmethod
    def handle_request(self, request: Request) -> Response:
        """Processes a Request and returns a Response."""
        pass

class MusicAssistant(AIAssistant):
    """Handles music recommendation requests."""
    def handle_request(self, request: Request) -> Response:
        if request.command_type == CommandType.RECOMMEND_MUSIC:
            return self.recommend_playlist(request)
        return Response("Sorry, cannot handle that request.", 0.0, False)

    def recommend_playlist(self, request: Request) -> Response:
        """
        Builds a simple playlist based on user mood.
        """
        mood = self.profile.preferences.get('mood', 'neutral')
        songs = [f"Song_{mood}_1", f"Song_{mood}_2"]
        msg = f"Recommended playlist based on mood '{mood}': {songs}"
        return Response(msg, confidence=0.9, action_performed=True)

class FitnessAssistant(AIAssistant):
    """Handles workout suggestion requests."""
    def handle_request(self, request: Request) -> Response:
        if request.command_type == CommandType.SUGGEST_WORKOUT:
            return self.suggest_workout(request)
        return Response("Sorry, request not recognized.", 0.0, False)

    def suggest_workout(self, request: Request) -> Response:
        """
        Suggests a workout plan based on user-defined fitness goals.
        """
        goal = self.profile.preferences.get('fitness_goal', 'general fitness')
        plan = f"30 minutes of {goal} exercises"
        msg = f"Suggested workout: {plan}"
        return Response(msg, confidence=0.85, action_performed=True)

class StudyAssistant(AIAssistant):
    """Handles study session scheduling requests."""
    def handle_request(self, request: Request) -> Response:
        if request.command_type == CommandType.SCHEDULE_STUDY:
            return self.schedule_study_session(request)
        return Response("Unable to handle that request.", 0.0, False)

    def schedule_study_session(self, request: Request) -> Response:
        """
        Schedules a study session for a given topic.
        """
        topic = self.profile.preferences.get('study_topic', 'general topics')
        time_str = request.timestamp.strftime("%Y-%m-%d %H:%M")
        msg = f"Scheduled study session on '{topic}' at {time_str}"
        return Response(msg, confidence=0.8, action_performed=True)

# ============================================
# Part 3: Simulation and Driver Script
# ============================================

if __name__ == "__main__":
    # Initialize profiles
    users = [
        UserProfile("Alice", 30, {'mood': 'happy'}, True),
        UserProfile("Bob", 22, {'fitness_goal': 'cardio'}, False),
        UserProfile("Carol", 25, {'study_topic': 'object-oriented programming'}, False)
    ]

    # Instantiate assistants for each user
    assistants = [
        MusicAssistant(users[0]),
        FitnessAssistant(users[1]),
        StudyAssistant(users[2])
    ]

    # Simulated raw requests
    user_inputs = [
        "Can you play some music for me?",
        "I want a workout plan",
        "Please help me schedule a study session"
    ]

    # Process interactions: greeting, then user request, then response
    for assistant, user_input in zip(assistants, user_inputs):
        # Step 1: Assistant greeting
        greet_response = assistant.greet_user()
        print(greet_response.message)

        # Step 2: Echo the user request immediately after greeting
        print(f"User request: '{user_input}'")

        # Step 3: Handle request and output assistant's reply
        request_obj = Request(user_input, datetime.now())
        resp = assistant.handle_request(request_obj)
        print(resp.message)

        # Separator for readability
        print('-' * 60)  
