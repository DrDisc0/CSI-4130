import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

# ✅ Correct Gemini endpoint
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"

print("🔍 Using model:", GEMINI_MODEL)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/rewrite', methods=['POST'])
def rewrite_email():
    data = request.get_json()
    email_text = data.get('email_text')
    tone = data.get('tone')

    prompt = (
        f"You are an assistant that professionally rewrites emails. "
        f"Rewrite the following email to sound more {tone}, clear, concise, and professional. "
        f"Provide only one rewritten version and do not include explanations or multiple examples.\n\n"
        f"---\n{email_text}\n---"
    )

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    resp = requests.post(GEMINI_URL, json=payload)
    try:
        result = resp.json()
    except ValueError:
        print("❌ Non-JSON response:", resp.text)
        return jsonify({'error': 'Invalid response from Gemini API.'}), 500

    try:
        rewritten = result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print("⚠️ Error extracting response:", e)
        rewritten = f"⚠️ Could not extract text. Raw response:\n{result}"

    return jsonify({'rewritten_text': rewritten})

@app.route('/summarize', methods=['POST'])
def summarize_email():
    data = request.get_json()
    email_text = data.get('email_text')

    prompt = f"Summarize this email in 2-3 clear sentences highlighting the main points and key actions:\n\n{email_text}"

    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    resp = requests.post(GEMINI_URL, json=payload)
    try:
        result = resp.json()
    except ValueError:
        print("❌ Non-JSON response:", resp.text)
        return jsonify({'error': 'Invalid response from Gemini API.'}), 500

    try:
        summary = result["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        print("⚠️ Error extracting response:", e)
        summary = f"⚠️ Could not extract summary. Raw response:\n{result}"

    return jsonify({'summary': summary})


if __name__ == '__main__':
    app.run(debug=True)
