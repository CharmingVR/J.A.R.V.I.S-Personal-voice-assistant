# Installation Guide for J.A.R.V.I.S

## Quick Start

### Windows

```bash
# 1. Install Python 3.8 or higher from python.org

# 2. Open Command Prompt and navigate to the project folder
cd path\to\J.A.R.V.I.S-Personal-voice-assistant

# 3. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the assistant
python Xa_14_project1_jarvis_assistant.py
```

### macOS

```bash
# 1. Install Python 3.8 or higher (via Homebrew or python.org)
brew install python3  # If using Homebrew

# 2. Navigate to the project folder
cd path/to/J.A.R.V.I.S-Personal-voice-assistant

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the assistant
python Xa_14_project1_jarvis_assistant.py
```

### Linux (Ubuntu/Debian)

```bash
# 1. Install Python and system dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv
sudo apt-get install espeak portaudio19-dev python3-pyaudio

# 2. Navigate to the project folder
cd path/to/J.A.R.V.I.S-Personal-voice-assistant

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the assistant
python3 Xa_14_project1_jarvis_assistant.py
```

### Linux (Fedora)

```bash
# 1. Install Python and system dependencies
sudo dnf install python3 python3-pip espeak portaudio-devel

# 2. Navigate to the project folder
cd path/to/J.A.R.V.I.S-Personal-voice-assistant

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the assistant
python3 Xa_14_project1_jarvis_assistant.py
```

### Linux (Arch)

```bash
# 1. Install Python and system dependencies
sudo pacman -S python python-pip espeak portaudio

# 2. Navigate to the project folder
cd path/to/J.A.R.V.I.S-Personal-voice-assistant

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the assistant
python3 Xa_14_project1_jarvis_assistant.py
```

## Common Issues

### PyAudio Installation Issues

If `pip install -r requirements.txt` fails with PyAudio errors:

**macOS:**
```bash
brew install portaudio
pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' pyaudio
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install portaudio19-dev python3-dev
pip install pyaudio
```

**Windows:**
- Download pre-built wheel from: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
- Install with: `pip install PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl`

### Microphone Not Found

1. Check system audio settings
2. Ensure microphone is connected and enabled
3. Test microphone with system tools:
   - **Windows**: Settings > Sound > Input
   - **macOS**: System Preferences > Sound > Input
   - **Linux**: `alsamixer` or `pavucontrol`

### TTS Not Working

**Windows:** Install SAPI5 voices via Settings > Time & Language > Speech

**macOS:** Voices should work by default; restart if issues occur

**Linux:** Install espeak:
```bash
# Ubuntu/Debian
sudo apt-get install espeak

# Fedora
sudo dnf install espeak

# Arch
sudo pacman -S espeak
```

## Verification

After installation, test each component:

```bash
# Test Python
python --version

# Test required packages
python -c "import pyttsx3; import speech_recognition; import wikipedia; print('All modules imported successfully')"

# Test microphone
python -c "import speech_recognition as sr; print(sr.Microphone().list_microphone_indexes())"

# Run the assistant
python Xa_14_project1_jarvis_assistant.py
```

## Support

If you encounter issues:
1. Check the main README.md for troubleshooting
2. Verify all system dependencies are installed
3. Ensure you're using Python 3.8 or higher
4. Check that your internet connection is active
5. Create an issue on the GitHub repository with details
