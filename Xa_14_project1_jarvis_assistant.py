import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib
import platform
import sys

# Initialize text-to-speech engine with cross-platform support
def init_engine():
    """Initialize TTS engine based on the operating system"""
    system = platform.system()
    try:
        if system == 'Windows':
            engine = pyttsx3.init('sapi5')
        elif system == 'Darwin':  # macOS
            engine = pyttsx3.init('nspeech')
        else:  # Linux and others
            engine = pyttsx3.init('espeak')
    except Exception as e:
        print(f"Error initializing TTS engine for {system}: {e}")
        print("Falling back to default engine...")
        engine = pyttsx3.init()
    
    return engine

engine = init_engine()
voices = engine.getProperty('voices')

# Set voice (use first available voice)
if voices:
    engine.setProperty('voice', voices[0].id)
else:
    print("Warning: No voices available for TTS")

# Set speech rate and volume
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)


def speak(audio):
    """Text-to-speech function"""
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(f"Error speaking: {e}")


def wishMe():
    """Greet the user based on the time of day"""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good evening. I hope that you are having a great day today")
    speak("I am Jarvis sir. Please tell me how may i help you")


def takeCommand():
    """Take voice command from the user and return as string"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        try:
            audio = r.listen(source, timeout=5)
        except sr.RequestError:
            print("Could not request results; check your internet connection")
            return "None"
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except sr.UnknownValueError:
        print("Say that again please...")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "None"
    except Exception as e:
        print(f"Error: {e}")
        return "None"


def sendEmail(to, content):
    """Send an email via Gmail"""
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        # WARNING: Never hardcode credentials in production!
        # Use environment variables instead
        email = os.getenv('JARVIS_EMAIL', 'your_email@gmail.com')
        password = os.getenv('JARVIS_PASSWORD', 'your_password')
        
        if email == 'your_email@gmail.com' or password == 'your_password':
            speak("Please set your email and password in environment variables")
            print("Set JARVIS_EMAIL and JARVIS_PASSWORD environment variables")
            return
        
        server.login(email, password)
        message = f"Subject: Message from JARVIS\n\n{content}"
        server.sendmail(email, to, message)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(f"Error sending email: {e}")
        speak("Sorry, I am not able to send this email")


def search_on_google(query):
    """Search for a query on Google"""
    try:
        webbrowser.open(f"https://www.google.com/search?q={query}")
    except Exception as e:
        print(f"Error searching Google: {e}")


if __name__ == "__main__":
    print(f"Running on {platform.system()} {platform.release()}")
    print("Starting JARVIS Personal Voice Assistant...\n")
    
    try:
        wishMe()
        while True:
            query = takeCommand().lower()
            
            if query == "none":
                continue
            
            if 'wikipedia' in query:
                speak('searching Wikipedia....')
                query_text = query.replace("wikipedia", "").strip()
                try:
                    results = wikipedia.summary(query_text, sentences=2)
                    speak("According to wikipedia")
                    print(results)
                    speak(results)
                except wikipedia.exceptions.DisambiguationError:
                    speak("The search was ambiguous. Please be more specific.")
                except wikipedia.exceptions.PageError:
                    speak("Sorry, I could not find that page on Wikipedia.")
                except Exception as e:
                    print(f"Error searching Wikipedia: {e}")
            
            elif 'open youtube' in query:
                speak("Opening YouTube")
                webbrowser.open("https://www.youtube.com/")
            
            elif 'open google' in query:
                speak("Opening Google")
                webbrowser.open("https://www.google.com")
            
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")
                print(f"Sir, the time is {strTime}")
            
            elif 'open classroom' in query:
                speak("Opening Google Classroom")
                webbrowser.open("https://classroom.google.com/u/0/h")
            
            elif 'open bharatacharya' in query:
                speak("Opening Bharatacharya Education")
                webbrowser.open("https://www.bharatacharyaeducation.com/")
            
            elif 'email to' in query:
                try:
                    speak("What should i say?")
                    content = takeCommand()
                    if content != "None":
                        to = input("Enter recipient's email address: ")
                        sendEmail(to, content)
                except Exception as e:
                    print(f"Error: {e}")
                    speak("Sorry, I am not able to send this email")
            
            elif 'exit' in query or 'quit' in query:
                speak("Goodbye! Shutting down JARVIS.")
                print("JARVIS is shutting down...")
                sys.exit()
    
    except KeyboardInterrupt:
        print("\nJARVIS is shutting down...")
        speak("Shutting down")
        sys.exit()
    except Exception as e:
        print(f"An error occurred: {e}")
        speak("An error occurred. Shutting down.")
        sys.exit()
