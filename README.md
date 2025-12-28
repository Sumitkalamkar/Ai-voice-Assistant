

# 🧠 Jarvis – Voice-Based AI Assistant (Version 1)

Jarvis is a voice-controlled AI assistant built using Python. It listens for a wake word, understands spoken commands, and responds intelligently using the Google Gemini API with an offline AI fallback.
This project is inspired by the idea of building a real-world personal AI assistant like **Jarvis from Iron Man**.

**Current Version:** 1
**Goal:** To evolve Jarvis into a proper, fully capable AI assistant.

---

## ✨ Features (Version 1)

* Wake word detection (`"Jarvis"`)
* Speech-to-text using Google Speech Recognition
* Text-to-speech responses using gTTS
* Online AI responses via Google Gemini (streaming)
* Offline AI fallback using Ollama + Mistral
* Built-in commands:

  * Current time
  * Current date
  * Exit / sleep
* Continuous listening loop

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:**

  * speech_recognition
  * gTTS
  * pygame
  * google-generativeai
* **Offline LLM:** Ollama (Mistral model)

---

## 📁 Project Structure

```
jarvis-ai-assistant/
│
├── jarvis.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/jarvis-ai-assistant.git
cd jarvis-ai-assistant
```

### 2. Install Dependencies

```bash
pip install speechrecognition gtts pygame google-generativeai
```

> ⚠️ **Note:** PyAudio is required for microphone access.

---

## 🔑 Gemini API Setup

Update the following line in the source code:

```python
genai.configure(api_key="Your_api_key")
```

Replace `"Your_api_key"` with your actual **Google Gemini API key**.

---

## 📴 Offline AI Setup (Optional)

Install Ollama and pull the Mistral model:

```bash
ollama pull mistral
```

Ensure `ollama` is available in your system PATH.

---

## ▶️ Running the Assistant

```bash
python jarvis.py
```

Say **"Jarvis"** to activate the assistant.

---

## 🧪 Example Commands

* Jarvis, what is the time?
* Jarvis, what is today’s date?
* Jarvis, explain artificial intelligence
* Jarvis, go to sleep

---

## 🧠 How It Works

1. Continuously listens for the wake word
2. Activates command mode
3. Processes built-in commands locally
4. Generates AI responses using Gemini
5. Falls back to offline AI if needed
6. Converts responses to speech

---

## ⚠️ Limitations (Version 1)

* No long-term memory
* No system automation
* Single wake word
* Limited command handling
* No graphical interface

---

## 🚀 Future Roadmap

* Contextual and long-term memory
* Desktop and system automation
* Plugin-based command architecture
* Web search integration
* Task scheduling and reminders
* Multi-language support
* Improved offline reasoning
* GUI dashboard

---

## 🎯 Project Vision

The aim of this project is to build a **proper AI assistant like Jarvis**, capable of understanding, reasoning, and executing real-world tasks.

---

## 👤 Author

**Sumit Kalamkar**
B.Tech – Artificial Intelligence & Machine Learning

---

## 📜 License

This project is open-source and intended for learning and experimentation.

