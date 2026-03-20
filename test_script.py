# test_script.py

from utils import extract_bullets
from analyzer import analyze_bullet

text = """
Responsible for improving website performance
Worked on developing APIs
Assisted team with data analysis
"""

bullets = extract_bullets(text)

for b in bullets:

    result = analyze_bullet(b)

    print(result)