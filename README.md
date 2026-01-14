# 🤖 J.A.R.V.I.S: AI-Powered Task Automation Through Voice

**J.A.R.V.I.S (Just A Rather Very Intelligent System)** is a web-based intelligent assistant that enables users to interact with their computer using **voice and text commands**. It acts as a centralized automation hub, simplifying everyday workflows by executing system tasks, monitoring resources, and responding intelligently through conversational AI.

---

## 🖼️ Application Screenshots

<img src="https://github.com/user-attachments/assets/5f88eda8-35f2-452c-9f46-0d9f1c1ca575" width="900" />
<img src="https://github.com/user-attachments/assets/71a54904-f4de-4985-bc25-368c18560dc0" width="900" />
<img src="https://github.com/user-attachments/assets/be73f051-7362-48cc-acff-7822a15317ad" width="900" />
<img src="https://github.com/user-attachments/assets/3a929ca7-3a8a-4004-90ac-2e4563063929" width="900" />

---

## 🚀 Key Features

* **Voice & Text Control**
  Accepts commands via microphone using the **Web Speech API** or through manual text input.

* **Task Automation**
  Launches local applications (e.g., Notepad, Calculator) and opens websites (e.g., Google, YouTube) using keyword-based commands.

* **Conversational AI**
  Integrated with **OpenAI GPT-3.5 Turbo** to handle natural language queries beyond predefined commands.

* **Real-Time System Monitoring**
  Displays live **CPU, RAM, and Disk usage** using the `psutil` library.

* **Futuristic UI**
  Cyberpunk-inspired, responsive interface featuring the **Orbitron font**, dark theme, and glowing visual elements.

* **Command Logging**
  Automatically records user commands and system responses in a `logs.txt` file for debugging and analysis.

---

## 🛠️ Technology Stack

### 🔹 Backend

* **Python**
* **Flask** – Application logic and API routing

### 🔹 Frontend

* **HTML5, CSS3, JavaScript**
* Web-based dashboard with real-time updates

### 🔹 AI Integration

* **OpenAI API (GPT-3.5 Turbo)** via **OpenRouter**

### 🔹 System & Utility Libraries

* `psutil` – System resource monitoring
* `subprocess` – Local application execution
* `webbrowser` – Website automation

### 🔹 Voice API

* **Web Speech API** for browser-based speech recognition

---

## 📂 System Architecture

The project follows a **modular client-server architecture**:

1. **Client Layer**
   Web interface where users interact using voice or text commands.

2. **Application Layer**
   Flask server that processes requests and routes them to appropriate modules.

3. **Processing Layer**
   Determines whether to execute a system command or forward the query to the conversational AI engine.

---

## 🔧 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Jarvis-AI-Voice-Assistant.git
cd Jarvis-AI-Voice-Assistant
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the application

```bash
python app.py
```

### 4️⃣ Access the assistant

Open your browser and navigate to:
👉 **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 🎓 Author

**Muhammad Arman**
Software Engineer
Bachelor of Science in Software Engineering
*University of Sahiwal*

---
