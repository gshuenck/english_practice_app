import speech_recognition as sr
import pyttsx3
import random
from difflib import SequenceMatcher


class EnglishPracticeApp:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.score = 0
        self.practice_phrases = [
            "Hello, how are you today?",
            "I would like to improve my English",
            "Could you please help me with directions?",
            "The weather is beautiful today",
            "I enjoy learning new languages"
        ]

    def text_to_speech(self, text):
        """Convert text to speech"""
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_to_speech(self):
        """Listen to user's speech and convert to text"""
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio)
                return text.lower()
            except sr.UnknownValueError:
                print("Sorry, I couldn't understand that.")
                return None
            except sr.RequestError:
                print("Sorry, there was an error with the speech recognition service.")
                return None

    def calculate_similarity(self, text1, text2):
        """Calculate similarity between two texts"""
        return SequenceMatcher(None, text1.lower(), text2.lower()).ratio()

    def practice_pronunciation(self):
        """Practice pronunciation with random phrases"""
        phrase = random.choice(self.practice_phrases)
        print(f"\nPlease say: {phrase}")
        self.text_to_speech(phrase)

        user_speech = self.listen_to_speech()
        if user_speech:
            similarity = self.calculate_similarity(phrase, user_speech)
            score = int(similarity * 100)
            self.score += score

            print(f"\nYou said: {user_speech}")
            print(f"Accuracy: {score}%")

            if score >= 90:
                print("Excellent pronunciation!")
            elif score >= 70:
                print("Good job! Keep practicing!")
            else:
                print("Let's try again to improve!")

    def run(self):
        """Run the application"""
        print("Welcome to English Speaking Practice!")
        while True:
            print("\n1. Practice pronunciation")
            print("2. View score")
            print("3. Exit")

            choice = input("\nEnter your choice (1-3): ")

            if choice == '1':
                self.practice_pronunciation()
            elif choice == '2':
                print(f"\nYour current score: {self.score}")
            elif choice == '3':
                print("\nThank you for practicing! Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    app = EnglishPracticeApp()
    app.run()