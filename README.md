# ✉️ AI Email Rewriter & Summarizer
**Author:** Collin Follett  
**Course:** CSI-4130/5130 — Artificial Intelligence  
**Project Theme:** AI in the Era of Generative Models  

---

## 🧠 Overview
The **AI Email Rewriter & Summarizer** is a Flask-based web app that uses modern **Generative AI** to help users quickly rewrite or summarize emails for improved **clarity**, **tone**, and **professionalism**.  

This project demonstrates the integration of **Large Language Models (LLMs)** through the **OpenRouter API**, providing a real-world example of how AI can enhance digital communication.  

---

## 🚀 Features
✅ Rewrite emails in different tones (Professional, Friendly, Concise, Apologetic)  
✅ Summarize long emails into short, clear summaries  
✅ Automatically formatted, easy-to-read interface  
✅ Responsive design with expanding result box  
✅ Built with Flask, HTML, CSS, and JavaScript  

---

## 🗂️ Project Structure
AIProject/
│
├── app.py # Flask backend
├── requirements.txt # Dependencies
├── .env.example # Example environment file (no real API key)
├── templates/
│ └── index.html # Frontend HTML
├── static/
│ └── style.css # Styling
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
4️⃣ Create a .env File
Create a new file named .env in the root folder and add:

ini
Copy code
OPENROUTER_API_KEY=sk-or-v1-your_key_here
OPENROUTER_API_BASE=https://openrouter.ai/api/v1
(You can get your key at https://openrouter.ai/keys)

🧩 How to Use the App
1️⃣ Run the Flask app:

bash
Copy code
python app.py
2️⃣ Open your browser and go to:

cpp
Copy code
http://127.0.0.1:5000
3️⃣ Paste or write an email in the textbox.
4️⃣ Select a tone (Professional, Friendly, etc.).
5️⃣ Click Rewrite Email or Summarize Email.
6️⃣ Your result will appear below with clean formatting.

🧱 Technologies Used
Python (Flask)

HTML5 / CSS3 / JavaScript

OpenRouter API (LLM integration)

dotenv for environment variables

🔒 Security Notes
Never upload your .env file to GitHub — it contains your private API key.

This project includes a .env.example file for demonstration only.

Add .env to your .gitignore to keep your credentials safe.

🧾 Example
Here’s what the app looks like in action:
(Insert screenshot here — for example:)

🧑‍💻 Future Improvements
Add export option (PDF or TXT)

Add grammar-checking and tone analysis

Deploy to a live web host for demo

🏁 Conclusion
This project showcases how Generative AI can be used to improve communication clarity and tone.
It combines user-friendly design with powerful AI backends to deliver a functional, real-world productivity tool.

📜 License
This project is open source and free to use for educational purposes.

pgsql
Copy code

---


It will render *beautifully* on GitHub — headers are consistent, code blocks display correctly, and everything is properly separated.

Would you like me to add your actual screenshot into it (so it shows up on your GitHub page)? I can write the correct line for your image once you tell me the filename or location of the screenshot (e.g., `static/demo.png`)
