import speech_recognition as sr
import datetime
import google.generativeai as genai
from gtts import gTTS
import os
import tempfile
import pygame
import subprocess
import sys
sys.stdout.reconfigure(encoding='utf-8')


class Jarvis:
    def __init__(self):
        self.name = "Jarvis"
        self.recognizer = sr.Recognizer()
        pygame.mixer.init()

        genai.configure(api_key="Your_api_key")

        self.model = genai.GenerativeModel(
            model_name="models/gemini-1.5-flash",
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 200
            },
            system_instruction=(
                "You are Jarvis, a helpful AI assistant. "
                "Answer clearly and directly. "
                "Do not say 'tell me more'."
            )
        )
        self.chat = self.model.start_chat(history=[])

        self.speak("Jarvis initialized. Waiting for wake word.")

    # ---------------- SPEECH ----------------
    def speak(self, text):
        print(f"Jarvis: {text}")
        tts = gTTS(text=text, lang='en')
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            path = fp.name
            tts.save(path)

        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pass
        pygame.mixer.music.unload()
        os.remove(path)

    # ---------------- LISTEN ----------------
    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=0.3)
            try:
                audio = self.recognizer.listen(source, timeout=8)
                return self.recognizer.recognize_google(audio)
            except:
                return ""

    # ---------------- WAKE WORD ----------------
    def wake_word_detected(self, text):
        return "jarvis" in text.lower()

    # ---------------- COMMAND HANDLER ----------------
    def handle_command(self, cmd):
        cmd = cmd.lower()

        if "time" in cmd:
            return f"It is {datetime.datetime.now().strftime('%I:%M %p')}"

        if "date" in cmd:
            return f"Today is {datetime.datetime.now().strftime('%A %B %d')}"

        if "sleep" in cmd or "exit" in cmd:
            self.speak("Going to sleep.")
            return "EXIT"

        return None

    # ---------------- OFFLINE LLM ----------------
    def offline_llm(self, prompt):
        try:
            result = subprocess.run(
                ["ollama", "run", "mistral"],
                input=prompt,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",        
                errors="ignore"          
            )
            return result.stdout.strip()
        except Exception as e:
            print("Offline LLM error:", e)
            return "Offline AI is currently unavailable."


    # ---------------- STREAMING GEMINI ----------------
    def gemini_stream(self, prompt):
        response_text = ""
        try:
            for chunk in self.model.generate_content(prompt, stream=True):
                if chunk.text:
                    response_text += chunk.text
            return response_text
        except:
            return self.offline_llm(prompt)

    # ---------------- MAIN LOOP ----------------
    def run(self):
        print("Sleeping... Say 'Jarvis'")

        # Wake word loop
        while True:
            text = self.listen()
            if self.wake_word_detected(text):
                self.speak("Yes?")
                break

        # Active loop
        while True:
            command = self.listen()
            if not command:
                continue

            result = self.handle_command(command)
            if result == "EXIT":
                break

            if result:
                self.speak(result)
                continue

            response = self.gemini_stream(command)
            self.speak(response)

        self.run()  


# ---------------- START ----------------
if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()
