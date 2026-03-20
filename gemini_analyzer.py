from google import genai
import os

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def improve_bullet(bullet):
    prompt = f"""
    You are a resume expert.

    Improve the following resume bullet point by:
    - Using a strong action verb
    - Adding measurable impact
    - Making it concise and ATS-friendly

    Bullet:
    {bullet}

    Return ONLY the improved bullet point.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text.strip()