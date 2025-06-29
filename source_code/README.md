# 🧠 AI Assistant Prototype – Assignment 2: Project Check-in 1

## 📌 Overview
This project is a prototype of an AI assistant, built in **Python**, to demonstrate:

- Use of **primitive and complex data types**
- Application of **Object-Oriented Programming** (OOP) concepts like encapsulation, inheritance, and polymorphism
- Basic **intent classification** via rule-based parsing
- Structured **response generation** with confidence scoring

The system simulates the functionality of assistants like **Siri**, **ChatGPT**, or **Alexa**, but without any third-party APIs or pre-trained models. It is built from scratch for educational purposes.

---

## ✅ Features at a Glance

| Feature                | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| Custom Data Types      | `UserProfile`, `Request`, `Response`                                        |
| Command Parser         | Regex-based function to classify natural input to `CommandType` enum        |
| AI Assistant Base      | `AIAssistant` abstract base class with `greet_user()` and `handle_request()` |
| Subclasses             | `MusicAssistant`, `FitnessAssistant`, `StudyAssistant`                      |
| Polymorphism           | Each subclass customizes `handle_request()` behavior                        |
| Confidence Scoring     | All responses include `confidence` score [0.0 – 1.0]                         |
| Output Format          | Clear interaction logs: Greeting → User Request → Assistant Response        |

---

## 🗂️ Project Structure
```
ai-assistant-checkin1/
├── source_code/
│   ├── ai_assistant.py     # Main implementation of assistant classes and simulation
│   └── README.md           # Documentation (this file)
```

---

## 🚀 How to Run the Program

### 🔧 Prerequisites
- Python **3.7+** installed

### ▶️ Steps to Execute
1. **Clone the repository**
```bash
git clone https://github.com/zazorus777/Assignment-2---AI-Assistant-Prototype.git
cd ai-assistant-checkin1/source_code
```

2. **Run the Python script**
```bash
python ai_assistant.py
```

3. **Observe the output** in your terminal:
```
Hello, Alice! How can assistance begin today?
User request: 'Can you play some music for me?'
Recommended playlist based on mood 'happy': ['Song_happy_1', 'Song_happy_2']
------------------------------------------------------------
Hello, Bob! How can assistance begin today?
User request: 'I want a workout plan'
Suggested workout: 30 minutes of cardio exercises
------------------------------------------------------------
Hello, Carol! How can assistance begin today?
User request: 'Please help me schedule a study session'
Scheduled study session on 'object-oriented programming' at 2025-06-26 22:03
------------------------------------------------------------
```

---

## 📘 Key Classes and Behaviors

### 🔹 `UserProfile`
Stores user-specific data:
```python
UserProfile(name: str, age: int, preferences: dict, is_premium: bool)
```

### 🔹 `Request`
Captures a user's request:
```python
Request(input_str: str, timestamp: datetime, command_type: CommandType)
```
- Uses `parse_intent()` to classify text if no command type is provided.

### 🔹 `Response`
Returned by assistant logic:
```python
Response(message: str, confidence: float, action_performed: bool)
```

### 🔹 `CommandType`
An Enum used for classification:
```python
class CommandType(Enum):
    RECOMMEND_MUSIC
    SUGGEST_WORKOUT
    SCHEDULE_STUDY
    UNKNOWN
```

---

## 🏗️ AI Assistant Hierarchy

### 🔸 `AIAssistant` (abstract class)
- `greet_user()` → returns welcome message
- `handle_request(request)` → overridden by subclasses

### 🔸 `MusicAssistant`
- Recommends a song playlist based on `preferences['mood']`

### 🔸 `FitnessAssistant`
- Suggests a fitness plan based on `preferences['fitness_goal']`

### 🔸 `StudyAssistant`
- Schedules study based on `preferences['study_topic']`

---

## 🔍 Parsing and Confidence Scoring

### 🧩 Intent Classification
```python
def parse_intent(input_str: str) -> CommandType:
    # Uses regex to map user input to known command types
```
- Maps inputs like "play music" to `RECOMMEND_MUSIC`
- Ensures flexibility in natural input processing

### 📈 Confidence Levels
Each assistant's response includes a confidence score:
- Music: **0.90**
- Fitness: **0.85**
- Study: **0.80**
- Errors/default: **0.0**

---

## 📚 Learning Outcomes

- Demonstrated OOP concepts clearly:
  - **Encapsulation**: Each class models a concept
  - **Inheritance**: Subclasses inherit from `AIAssistant`
  - **Polymorphism**: `handle_request()` behaves differently across assistants

- Emulated real-world AI assistant behavior with structured design
- Validated data inputs for type safety and logical consistency
- Simulated user interactions cleanly and understandably

---

## 🧾 Summary of Requirements Fulfilled

| Requirement Section         | Fulfilled? | Details                                       |
|-----------------------------|------------|-----------------------------------------------|
| Data Types + Validation     | ✅         | Implemented `UserProfile`, `Request`, `Response`, `Enum` with full validation |
| OOP Structure               | ✅         | Abstract base class + 3 subclasses with unique behavior |
| Polymorphism                | ✅         | Each assistant handles `handle_request()` differently |
| Simulation & User Handling  | ✅         | 3 users simulated with clean input/output mapping |
| Parsing Logic               | ✅         | Regex-based intent classification fully implemented |
| Confidence Scoring          | ✅         | Built into `Response` class                   |
| No external AI model used   | ✅         | All logic is hand-coded for educational clarity |

---

## 📬 Contact
For any issues or clarification:
- Email: `khakobyan@cpp.edu`
