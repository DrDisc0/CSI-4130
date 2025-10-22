# ✉️ AI Email Rewriter & Summarizer
**Author:** Collin Follett  
**Course:** CSI-4130/5130 — Artificial Intelligence  
**Project Theme:** AI in the Era of Generative Models  

---

## 🧠 Overview
The **AI Email Rewriter & Summarizer** is a Flask-based web application that uses **Google’s Gemini 2.5 AI model** to help users rewrite and summarize emails for improved **clarity**, **tone**, and **professionalism**.  

This project demonstrates the real-world use of **Large Language Models (LLMs)** to enhance everyday communication and productivity through simple natural language interaction.

---

## 🚀 Features
✅ Rewrite emails in various tones (Professional, Friendly, Concise, Apologetic)  
✅ Summarize long emails into short, focused summaries  
✅ Clean, responsive user interface  
✅ Expanding output box for readable results  
✅ 100% free and powered by **Google’s Gemini API**  

---

## 🗂️ Project Structure
AIProject/
│
├── app.py # Flask backend logic
├── requirements.txt # Dependencies
├── templates/
│ └── index.html # Frontend HTML
├── static/
│ └── style.css # Styling and layout
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/AIProject.git
cd AIProject
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the App
bash
Copy code
python app.py
5️⃣ Open in Browser
Visit:

cpp
Copy code
http://127.0.0.1:5000
Then:

Paste or type your email.

Choose a tone (Professional, Friendly, etc.).

Click Rewrite Email or Summarize Email.

View your improved or summarized email below.

🧱 Technologies Used
Python (Flask) — Backend web framework

HTML / CSS / JavaScript — Frontend and interactivity

Google Gemini 2.5 API — AI model for rewriting and summarization

🧑‍💻 Future Improvements
Add grammar and tone analysis tools

Support exporting results (PDF, TXT, or email draft)

Optional Chrome/Outlook plugin integration

Add Gemini “Pro” mode toggle for higher-quality responses

🏁 Conclusion
This project showcases how Generative AI can enhance real-world communication through natural language processing.
By integrating Gemini 2.5, the app delivers intelligent, context-aware rewriting and summarization with a simple and elegant interface.

📜 License
Open source and free for educational use.
Developed by Collin Follett for CSI-4130/5130: Artificial Intelligence.
