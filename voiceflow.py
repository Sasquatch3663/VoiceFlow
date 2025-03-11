import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound

def speech_to_text():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Please say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said: " + text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def text_to_speech(text, lang='en'):
    if text:
        tts = gTTS(text=text, lang=lang)
        filename = "output.mp3"
        tts.save(filename)
        print("Playing the audio...")
        playsound(filename)
        # Optionally, ask the user if they want to delete the file
        if input("Delete the audio file after playing? (y/n): ").lower() == 'y':
            os.remove(filename)

def main():
    while True:
        print("\nChoose an option:")
        print("1. Convert Speech to Text")
        print("2. Convert Text to Speech")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            speech_to_text()
        elif choice == '2':
            text = input("Enter the text you want to convert to speech: ")
            lang = input("Enter the language code (default is 'en'): ") or 'en'
            text_to_speech(text, lang)
        elif choice == '3':
            if input("Are you sure you want to exit? (y/n): ").lower() == 'y':
                print("Exiting the program.")
                break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
