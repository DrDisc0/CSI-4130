# ✉️ AI Email Rewriter & Summarizer
**Author:** Collin Follett  
**Course:** CSI-4130/5130 — Artificial Intelligence  
**Project Theme:** AI in the Era of Generative Models  

---

## 🧠 Overview
The **AI Email Rewriter & Summarizer** is a Flask-based web app powered by **Google’s Gemini 2.5 AI model**.  
It helps users rewrite or summarize emails with improved **clarity**, **tone**, and **professionalism**.  

This project demonstrates practical use of **Large Language Models (LLMs)** for enhancing everyday communication and productivity.

---

## 🚀 Features
- ✅ Rewrite emails in various tones (Professional, Friendly, Concise, Apologetic)  
- ✅ Summarize long emails into short, focused summaries  
- ✅ Clean, responsive UI with auto-expanding result box  
- ✅ 100 % free — powered by **Google Gemini API**

---

## 🗂️ Project Structure
```
AIProject/
│
├── app.py                 # Flask backend logic
├── requirements.txt       # Dependencies
├── templates/
│   └── index.html         # Frontend HTML
├── static/
│   └── style.css          # Styling and layout
└── README.md              # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/AIProject.git
cd AIProject
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate   # macOS / Linux
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App
```bash
python app.py
```

### 5️⃣ Open in Browser
Visit → [http://127.0.0.1:5000](http://127.0.0.1:5000)

Then:
1. Paste or type your email.  
2. Choose a tone (Professional, Friendly, etc.).  
3. Click **Rewrite Email** or **Summarize Email**.  
4. View your improved or summarized email below.  

---

## 🧱 Technologies Used
- **Python (Flask)** — Backend web framework  
- **HTML / CSS / JavaScript** — Frontend and interactivity  
- **Google Gemini 2.5 API** — AI model for rewriting and summarization  

---

## 🧑‍💻 Future Improvements
- Add grammar and tone analysis tools  
- Support exporting results (PDF / TXT / email draft)  
- Optional Chrome / Outlook plugin integration  
- Add **Gemini Pro mode** toggle for higher-quality results  

---

## 🏁 Conclusion
This project shows how **Generative AI** can enhance real-world communication through natural-language processing.  
By integrating **Gemini 2.5**, the app provides intelligent, context-aware rewriting and summarization with a simple, elegant interface.  

---

## 📜 License
Open source and free for educational use.  
Developed by **Collin Follett** for **CSI-4130/5130: Artificial Intelligence**.
