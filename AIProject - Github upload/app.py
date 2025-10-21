from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI
import traceback

load_dotenv()

app = Flask(__name__)

# ✅ Setup OpenRouter client
client = OpenAI(
    base_url=os.getenv("OPENROUTER_API_BASE"),
    api_key=os.getenv("OPENROUTER_API_KEY")
)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/rewrite', methods=['POST'])
def rewrite_email():
    data = request.get_json()
    email_text = data.get('email_text')
    tone = data.get('tone')

    prompt = f"Rewrite this email to sound more {tone}. Keep it clear, concise, and professional:\n\n{email_text}"

    try:
        response = client.chat.completions.create(
            model="mistralai/mixtral-8x7b-instruct",
            messages=[
                {"role": "system", "content": "You are an expert email writing assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        rewritten_text = response.choices[0].message.content.strip()
        return jsonify({'rewritten_text': rewritten_text})

    except Exception as e:
        traceback.print_exc()
        print("API call failed:", e)
        return jsonify({'error': str(e)}), 500


@app.route('/summarize', methods=['POST'])
def summarize_email():
    data = request.get_json()
    email_text = data.get('email_text')

    prompt = f"Summarize the following email in 2–3 concise, professional sentences, highlighting key points and tone:\n\n{email_text}"

    try:
        response = client.chat.completions.create(
            model="mistralai/mixtral-8x7b-instruct",
            messages=[
                {"role": "system", "content": "You are an expert email summarizer."},
                {"role": "user", "content": prompt}
            ]
        )

        summary = response.choices[0].message.content.strip()
        return jsonify({'summary': summary})

    except Exception as e:
        traceback.print_exc()
        print("API call failed:", e)
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
