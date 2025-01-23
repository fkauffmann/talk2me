# Talk2Me

**Talk to an IA and let it answer to you!**

This script is a very basic interactive voice-based Q&A system. 

It captures user input via audio recording until the ENTER key is pressed. The recorded audio is then transcribed to text. 

Using this transcribed text, the script generates a prompt for a local Large Language Model (LLM) running on OLLAMA. 

After receiving the LLM's generated response, the text is converted to an MP3 audio file, which is then played back using Pygame, creating a complete voice interaction loop.

## Installation

### 1. Install OLLAMA

Install OLLAMA on Ubuntu using the following command:

```
sudo curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Download the LLM

Download the large language model of your choice. For example:

```
ollama pull llama3.2:3b
```

### 3. Create a virtual environment for Python

```
mkdir talk2me
cd talk2me
python3 -m venv .venv
cd .venv
cd bin
source activate
cd ../..
```

## 4. Install the required libraries

The following Python libraries are required to run the script
``` 
sudo apt-get install libportaudio2
pip install numpy pynput
pip install sounddevice scipy SpeechRecognition
pip install ollama
pip install gTTS
pip install pygame
```

## Usage

Just run the script!

```
python app.py
```
