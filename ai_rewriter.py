# ai_rewriter.py

import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY") or st.secrets["GOOGLE_API_KEY"]

client = genai.Client(api_key=api_key)

#client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def rewrite_bullet_ai(bullet):

    prompt = f"""
You are an expert resume writer.

Rewrite the resume bullet to make it stronger.

Rules:
- Use strong action verbs
- Do NOT invent numbers or metrics
- Keep bullets concise
- Return ONLY JSON

Format exactly like this:

{{
  "bullets": [
    "bullet 1",
    "bullet 2",
    "bullet 3"
  ]
}}

Bullet:
{bullet}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    # remove markdown code blocks if Gemini adds them
    text = text.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(text)
        return data["bullets"]

    except Exception as e:
        print("Gemini response:", text)
        return ["Parsing failed"]