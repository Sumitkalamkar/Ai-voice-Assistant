🤖 Jarvis – AI Voice Assistant (Python)

Jarvis is a voice-controlled AI assistant built using Python that can listen to your voice, understand commands, answer questions using Google Gemini AI, and fall back to an offline LLM (Ollama) when the internet is unavailable.

It supports:

🎤 Voice input

🧠 AI-powered responses

🗣️ Text-to-speech output

💤 Wake-word activation (“Jarvis”)

📴 Offline AI fallback

⏰ Built-in system commands (time, date, exit)

✨ Features

Wake Word Detection
Jarvis stays idle until you say “Jarvis”.

Command + Chat Hybrid

Commands like time, date, sleep are handled instantly.

All other queries go to AI.

Online AI (Gemini 1.5 Flash)

Fast, accurate answers.

Streaming response support.

Offline AI Fallback

Uses Ollama + Mistral if Gemini fails or internet is down.

Text-to-Speech

Converts AI responses into natural voice using gTTS.

🧠 Architecture Overview
Microphone
   ↓
Wake Word Detection ("Jarvis")
   ↓
Command Router
   ├── System Commands (time, date, exit)
   ├── Gemini AI (online)
   └── Ollama LLM (offline)
   ↓
Text-to-Speech (gTTS)
   ↓
Speaker Output

🛠️ Technologies Used

Python 3.9+

speech_recognition

google-generativeai (Gemini)

gTTS

pygame

Ollama (offline LLM)

subprocess

📦 Installation
1️⃣ Clone the Repository
git clone https://github.com/your-username/jarvis-ai.git
cd jarvis-ai

2️⃣ Install Python Dependencies
pip install speechrecognition google-generativeai gTTS pygame pyaudio


⚠️ Windows users (PyAudio issue)

pip install pipwin
pipwin install pyaudio

🧠 Offline AI Setup (Optional but Recommended)
Install Ollama

👉 https://ollama.com

Pull a model
ollama pull mistral

Warm-up (run once)
ollama run mistral

🔑 Gemini API Key Setup

Visit: https://aistudio.google.com/app/apikey

Generate an API key

Paste it in the code:

genai.configure(api_key="YOUR_API_KEY_HERE")


⚠️ Never commit your API key to GitHub

▶️ How to Run
python jarvis.py

🗣️ How to Use

Start the program

Say “Jarvis”

Ask questions or give commands:

Example Commands

“What is machine learning?”

“What is the time?”

“What is today’s date?”

“Explain neural networks”

“Sleep” / “Exit”

🧪 Example Interaction
You: Jarvis
Jarvis: Yes?

You: What is artificial intelligence?
Jarvis: Artificial intelligence enables machines to simulate human thinking and decision-making.

You: What is the time?
Jarvis: It is 10:45 AM

⚙️ Configuration Options

You can tune AI behavior here:

generation_config={
    "temperature": 0.7,
    "max_output_tokens": 200
}


Lower temperature → more factual answers

Fewer tokens → faster responses

🚀 Future Enhancements

🔐 Voice authentication

🧠 Long-term memory

🌐 Web search integration

🪟 Open applications via voice

⚡ Faster offline TTS

📦 Windows .exe build

🧑‍💻 Author

Sumit Kalamkar
B.Tech – Artificial Intelligence & Machine Learning

📄 License

This project is licensed under the MIT License.
Feel free to use, modify, and learn from it.
