# keyword_matcher.py

import re
from collections import Counter

COMMON_STOPWORDS = {
    "the","and","a","to","of","in","for","on","with","is","are",
    "as","an","be","by","this","that","from","or","at","it"
}


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text


def extract_keywords(text):

    text = clean_text(text)
    words = text.split()

    filtered = [
        w for w in words
        if w not in COMMON_STOPWORDS and len(w) > 2
    ]

    freq = Counter(filtered)

    keywords = [word for word, count in freq.most_common(20)]

    return keywords


def calculate_match_score(resume_text, job_description):

    resume_text = clean_text(resume_text)

    keywords = extract_keywords(job_description)

    matched = []
    missing = []

    for word in keywords:
        if word in resume_text:
            matched.append(word)
        else:
            missing.append(word)

    if len(keywords) == 0:
        return 0, [], []

    score = int((len(matched) / len(keywords)) * 100)

    return score, matched, missing