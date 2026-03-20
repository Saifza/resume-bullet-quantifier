# utils.py

import re


def extract_bullets(text):

    lines = text.split("\n")

    bullets = []

    bullet_patterns = [
        r"^\s*•",
        r"^\s*-",
        r"^\s*\*",
    ]

    for line in lines:

        line = line.strip()

        for pattern in bullet_patterns:

            if re.match(pattern, line):
                cleaned = re.sub(pattern, "", line).strip()

                if len(cleaned) > 40:
                    bullets.append(cleaned)

    return bullets