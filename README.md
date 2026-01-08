J.A.R.V.I.S: AI-Powered Task Automation Through Voice

J.A.R.V.I.S is a web-based intelligent assistant designed to provide a centralized hub for interacting with a computer through voice and text commands. It simplifies complex workflows by automating system tasks and integrating conversational AI.
+3

🚀 Key Features

Voice & Text Control: Users can provide commands via a microphone using the Web Speech API or by typing into a text field.
+2


Task Automation: Instantly launches local applications (e.g., Notepad, Calculator) and navigates to websites (e.g., Google, YouTube) based on keywords.
+1


Conversational AI: Integrated with OpenAI’s GPT-3.5 Turbo to handle natural language queries that do not match predefined commands.
+3


Real-time System Monitoring: A live dashboard displays CPU, RAM, and Disk usage metrics retrieved using the psutil library.
+3


Futuristic UI: A responsive "cyberpunk-inspired" interface featuring the Orbiton font and a dark, glowing aesthetic.
+1


Command Logging: Automatically records all user inputs and system responses to a logs.txt file for analysis.
+1

🛠️ Technology Stack

Backend Framework: Python with Flask.
+1


Frontend Technologies: HTML5, CSS3, JavaScript.
+1


AI Integration: OpenAI API (via OpenRouter).
+2


System Libraries: psutil for metrics, subprocess for launching apps, and webbrowser for web tasks.
+1


APIs: Web Speech API for browser-based voice recognition.
+1

📂 System Architecture
The project follows a modular client-server setup:


Client Layer: The "face" of the assistant where users interact via the web interface.
+1


Application Layer: A Flask server that acts as a bridge between user input and system modules.


Processing Layer: Decides whether to execute a local command or send the query to the conversational AI.
+1

🔧 Installation & Setup
Clone the Repository:

Bash

git clone https://github.com/your-username/Jarvis-AI-Voice-Assistant.git
cd Jarvis-AI-Voice-Assistant
Install Dependencies:

Bash

pip install -r requirements.txt
Run the Application:

Bash

python app.py

Access the Assistant: Open your browser and go to http://127.0.0.1:5000/.

🎓 Author
Muhammad Arman Software Engineer Bachelor of Science in Software Engineering


University of Sahiwal
