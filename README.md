# English Practice App

## Overview

The **English Practice App** is a simple Python application designed to help users improve their English pronunciation through interactive speech recognition. The app provides randomly selected phrases for the user to pronounce, evaluates their accuracy using speech recognition, and gives feedback on their performance.

## Features

- **Speech-to-Text Recognition**: Uses Google Speech Recognition to analyze user pronunciation.
- **Text-to-Speech**: Reads out phrases for the user to repeat.
- **Pronunciation Accuracy Scoring**: Compares user speech with the given phrase and calculates a similarity score.
- **Interactive Practice Mode**: Encourages users to improve through real-time feedback.
- **Score Tracking**: Keeps track of the user's progress over multiple practice sessions.

## Requirements

To run this app, you need to install the following dependencies:

```bash
pip install SpeechRecognition pyttsx3 PyAudio 
```

Additionally, ensure that you have a working **microphone** for speech recognition to function properly.

## Usage

1. **Run the application**

   ```bash
   python english_practice_app.py
   ```

2. **Select an option**

   - Press `1` to practice pronunciation.
   - Press `2` to view your current score.
   - Press `3` to exit the application.

3. **Practice pronunciation**

   - The app will present a phrase and read it aloud.
   - Speak the phrase into your microphone.
   - The app will analyze your speech and provide feedback on accuracy.

## How It Works

- The application randomly selects a phrase from a predefined list.
- It uses `pyttsx3` for text-to-speech conversion to read the phrase aloud.
- The user repeats the phrase, which is recorded and processed using `SpeechRecognition`.
- The similarity between the spoken phrase and the original is calculated using `difflib.SequenceMatcher`.
- A score is given based on pronunciation accuracy.

## Example Interaction

```
Welcome to English Speaking Practice!

1. Practice pronunciation
2. View score
3. Exit

Enter your choice (1-3): 1

Please say: Hello, how are you today?
Listening...

You said: hello how are you today
Accuracy: 95%
Excellent pronunciation!
```

## Future Improvements

- Add more phrases to expand vocabulary practice.
- Implement a leaderboard or progress tracking feature.
- Support multiple difficulty levels.
- Provide phonetic hints for better pronunciation guidance.

## License

This project is open-source and available for personal and educational use.

---

**Start improving your English pronunciation today!**