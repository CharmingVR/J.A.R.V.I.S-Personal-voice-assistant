# J.A.R.V.I.S Personal Voice Assistant

A cross-platform personal voice assistant built with Python. It listens to voice commands, responds using text-to-speech, and can perform common tasks such as opening websites, reading the current time, searching Wikipedia, and sending emails.

## Features

- ✅ Cross-platform support (Windows, macOS, Linux)
- 🎤 Voice command recognition using the microphone
- 🔊 Text-to-speech response with platform-specific engines
- 🔍 Wikipedia search
- 🌐 Open YouTube, Google, Classroom, Bharatacharya
- ⏰ Check current time
- 📧 Email sending support
- 👋 Smart greeting and assistant personality
- 🛡️ Error handling and graceful fallbacks

## Requirements

- Python 3.8 or higher
- Microphone access
- Internet connection for:
  - Google Speech Recognition
  - Wikipedia search
  - Web browsing

### Platform-Specific Requirements

#### Windows
- No additional system requirements (uses built-in SAPI5)

#### macOS
- No additional system requirements (uses built-in NSpeech)

#### Linux
- Install `espeak` for text-to-speech:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install espeak
  
  # Fedora
  sudo dnf install espeak
  
  # Arch
  sudo pacman -S espeak
  ```
- Install audio dependencies:
  ```bash
  # Ubuntu/Debian
  sudo apt-get install python3-pyaudio
  
  # Or use pip (if the above doesn't work)
  pip install pyaudio
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CharmingVR/J.A.R.V.I.S-Personal-voice-assistant.git
   cd J.A.R.V.I.S-Personal-voice-assistant
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Email Setup (Optional)

To enable email sending, set environment variables with your Gmail credentials:

```bash
# On Linux/macOS
export JARVIS_EMAIL="your_email@gmail.com"
export JARVIS_PASSWORD="your_app_password"  # Use Gmail App Password, not your regular password

# On Windows (Command Prompt)
set JARVIS_EMAIL=your_email@gmail.com
set JARVIS_PASSWORD=your_app_password

# On Windows (PowerShell)
$env:JARVIS_EMAIL="your_email@gmail.com"
$env:JARVIS_PASSWORD="your_app_password"
```

**Important**: Use [Gmail App Password](https://support.google.com/accounts/answer/185833) instead of your regular password for security.

## Running the Assistant

```bash
python Xa_14_project1_jarvis_assistant.py
```

The assistant will:
1. Greet you based on the time of day
2. Listen for voice commands
3. Execute commands or respond with information
4. Continue listening until you say "exit" or "quit"

## Voice Commands

- **"wikipedia [topic]"** - Search Wikipedia for a topic
- **"open youtube"** - Open YouTube in your default browser
- **"open google"** - Open Google in your default browser
- **"the time"** - Tell you the current time
- **"open classroom"** - Open Google Classroom
- **"open bharatacharya"** - Open Bharatacharya Education website
- **"email to"** - Send an email (requires configuration)
- **"exit" or "quit"** - Shutdown the assistant

## Troubleshooting

### Microphone Issues
- Ensure your microphone is properly connected and recognized by your OS
- Check microphone permissions in your system settings
- Test your microphone with system audio settings before running JARVIS

### Speech Recognition Not Working
- Verify you have an active internet connection
- Ensure microphone has sufficient audio level
- Try speaking more clearly and slowly
- Check firewall/VPN settings that might block Google's speech API

### TTS Not Working
- **Windows**: Check that SAPI5 voices are installed via Control Panel > Speech Recognition
- **macOS**: Built-in NSpeech should work; restart if needed
- **Linux**: Ensure `espeak` is installed: `sudo apt-get install espeak`

### Email Sending Issues
- Verify Gmail credentials are set correctly in environment variables
- Use [Gmail App Password](https://support.google.com/accounts/answer/185833) instead of account password
- Enable "Less secure app access" if using a regular password (not recommended)

## Project Structure

```
J.A.R.V.I.S-Personal-voice-assistant/
├── Xa_14_project1_jarvis_assistant.py  # Main assistant script
├── requirements.txt                     # Python dependencies
├── README.md                            # This file
└── python_project_JARVIS PERSONAL ASSISTANT.txt  # Additional documentation
```

## Security Notes

⚠️ **Important Security Considerations**:
- Never hardcode email credentials in the script
- Always use environment variables for sensitive information
- Use Gmail App Passwords instead of your account password
- Be cautious with voice commands that perform sensitive actions
- Keep dependencies updated: `pip install --upgrade -r requirements.txt`

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is provided as-is for educational and personal use.

## Disclaimer

This project was created as a learning/demo project. Use at your own risk and responsibility.
