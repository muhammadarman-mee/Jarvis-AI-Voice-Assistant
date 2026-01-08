from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
import subprocess
import webbrowser
import psutil
from datetime import datetime
import urllib.parse
import requests
import re

app = Flask(__name__)
CORS(app)
app.secret_key = "your-secret-key"

client = OpenAI(
    api_key="enter your api",  # ⚠️ Replace before deployment
    base_url="https://openrouter.ai/api/v1"
)

app_commands = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "word": "winword.exe",
    "excel": "excel.exe",
    "powerpoint": "powerpnt.exe",
    "cmd": "cmd.exe",
    "explorer": "explorer.exe",
    "chrome": "chrome.exe"
}

website_commands = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "twitter": "https://www.twitter.com",
    "facebook": "https://www.facebook.com",
    "amazon": "https://www.amazon.com",
    "linkedin": "https://www.linkedin.com",
    "github": "https://github.com"
}

# ---------------------------
# Add global chat memory
# ---------------------------
chat_history = []

def play_song(song_name):
    """Search YouTube and play the first matching video."""
    try:
        query = urllib.parse.quote(song_name)
        search_url = f"https://www.youtube.com/results?search_query={query}"
        html = requests.get(search_url).text
        match = re.search(r"watch\?v=(\S{11})", html)
        if match:
            video_id = match.group(1)
            youtube_url = f"https://www.youtube.com/watch?v={video_id}"
            webbrowser.open(youtube_url)
            return f"Playing {song_name} on YouTube."
        else:
            return f"Could not find a video for {song_name}."
    except Exception as e:
        return f"Error searching YouTube: {str(e)}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    data = request.get_json()
    user_input = data.get("command", "").lower()
    translated = user_input.strip()

    # --- 1. Play command ---
    if translated.startswith("play "):
        song_name = translated.replace("play", "", 1).strip()
        response = play_song(song_name) if song_name else "Please specify a song name."
        log_command(user_input, response)
        return jsonify({"response": response})

    # --- 2. Ends with 'song' ---
    if translated.endswith(" song"):
        song_name = translated.rsplit(" song", 1)[0].strip()
        response = play_song(song_name) if song_name else "Please specify a song name."
        log_command(user_input, response)
        return jsonify({"response": response})

    if "time" in translated:
        now = datetime.now().strftime("%H:%M")
        response = f"The current time is {now}."
        log_command(user_input, response)
        return jsonify({"response": response})

    if "write to file" in translated:
        content = translated.split("write to file", 1)[1].strip()
        with open("jarvis_notes.txt", "a", encoding="utf-8") as f:
            f.write(content + "\n")
        response = "Text written to file."
        log_command(user_input, response)
        return jsonify({"response": response})

    if "read file" in translated:
        if os.path.exists("jarvis_notes.txt"):
            with open("jarvis_notes.txt", "r", encoding="utf-8") as f:
                text = f.read()
            response = text
        else:
            response = "File not found."
        log_command(user_input, response)
        return jsonify({"response": response})

    # --- App open/close ---
    for app_name, command in app_commands.items():
        if f"open {app_name}" in translated:
            os.system(f"start {command}")
            response = f"Opening {app_name}."
            log_command(user_input, response)
            return jsonify({"response": response})
        elif f"close {app_name}" in translated:
            os.system(f"taskkill /f /im {command}")
            response = f"Closing {app_name}."
            log_command(user_input, response)
            return jsonify({"response": response})

    # --- Website commands ---
    for site, url in website_commands.items():
        if f"open {site}" in translated:
            webbrowser.open(url)
            response = f"Opening {site}."
            log_command(user_input, response)
            return jsonify({"response": response})

    # --- Search commands ---
    if "search" in translated:
        query = translated.replace("search", "").strip()

        if "on youtube" in query:
            yt_query = query.replace("on youtube", "").strip()
            url = f"https://www.youtube.com/results?search_query={yt_query.replace(' ', '+')}"
            webbrowser.open(url)
            response = f"Searching YouTube for '{yt_query}'."
            log_command(user_input, response)
            return jsonify({"response": response})

        elif "on amazon" in query:
            amz_query = query.replace("on amazon", "").strip()
            url = f"https://www.amazon.com/s?k={amz_query.replace(' ', '+')}"
            webbrowser.open(url)
            response = f"Searching Amazon for '{amz_query}'."
            log_command(user_input, response)
            return jsonify({"response": response})

        else:
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(url)
            response = f"Searching Google for '{query}'."
            log_command(user_input, response)
            return jsonify({"response": response})

    # ---------------------------
    # AI with memory
    # ---------------------------
    try:
        # Save user message to history
        chat_history.append({"role": "user", "content": translated})

        ai_response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are JARVIS, a helpful AI assistant with memory."}] + chat_history,
        )

        reply = ai_response.choices[0].message.content.strip()

        # Save assistant reply to history
        chat_history.append({"role": "assistant", "content": reply})

        log_command(user_input, reply)
        return jsonify({"response": reply})

    except Exception as e:
        error_message = f"AI Error: {str(e)}"
        log_command(user_input, error_message)
        return jsonify({"response": error_message})

def log_command(user_input, response):
    with open("logs.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | Input: {user_input} | Response: {response}\n")

@app.route("/system-info", methods=["GET"])
def system_info():
    info = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory": dict(psutil.virtual_memory()._asdict()),
        "disk": dict(psutil.disk_usage('/')._asdict()),
        "boot_time": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(info)

@app.route("/analyze-logs", methods=["GET"])
def analyze_logs():
    if not os.path.exists("logs.txt"):
        return jsonify({"response": "No logs found to analyze."})

    with open("logs.txt", "r", encoding="utf-8") as f:
        content = f.read()

    try:
        analysis = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You're a system assistant. Analyze and summarize the user's log."},
                {"role": "user", "content": content}
            ]
        )
        summary = analysis.choices[0].message.content.strip()
        return jsonify({"response": summary})
    except Exception as e:
        return jsonify({"response": f"AI analysis error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)

