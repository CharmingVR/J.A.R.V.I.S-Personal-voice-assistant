# J.A.R.V.I.S Personal Voice Assistant

This project is a personal voice assistant built with Python. It listens to voice commands, responds using text-to-speech, and can perform a few common tasks such as opening websites, reading the current time, and searching Wikipedia.

## Features

- Voice command recognition using the microphone
- Text-to-speech response using `pyttsx3`
- Wikipedia search
- Open YouTube/Google/Classroom/Bharatacharya
- Check current time
- Email sending support
- Greeting and assistant personality

## Requirements

- Python 3.8+
- Windows OS (this project uses `sapi5` for voice synthesis)
- Microphone access
- Internet connection for Google Speech Recognition and web browsing

## Installation

1. Clone the repository.
2. Open a terminal in the project folder.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the assistant

```bash
python Xa_14_project1_jarvis_assistant.py
```

## Notes

- This project was created as a learning/demo project.
- Some features such as sending email may require updating the email credentials inside the script.
- Voice recognition uses Google Speech Recognition, so an internet connection is required.

## Files

- `Xa_14_project1_jarvis_assistant.py` - main assistant script
- `requirements.txt` - Python dependencies
