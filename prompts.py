# prompts.py

def rewrite_prompt(bullet):

    return f"""
You are a professional resume writer.

Rewrite the following resume bullet point to be stronger.

Rules:
- Start with a strong action verb
- Use active voice
- Include measurable results if possible
- Keep the bullet concise
- Generate 3 improved versions

Bullet:
{bullet}
"""