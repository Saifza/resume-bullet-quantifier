# analyzer.py

from config import weak_verbs, generic_phrases
from scoring import score_bullet


def detect_weak_verbs(bullet):

    issues = []

    for weak in weak_verbs:
        if weak in bullet.lower():
            issues.append(weak)

    return issues


def detect_generic_phrases(bullet):

    issues = []

    for phrase in generic_phrases:
        if phrase in bullet.lower():
            issues.append(phrase)

    return issues


def analyze_bullet(bullet):

    weak = detect_weak_verbs(bullet)
    generic = detect_generic_phrases(bullet)

    score = score_bullet(bullet)

    return {
        "bullet": bullet,
        "weak_verbs": weak,
        "generic_phrases": generic,
        "score": score
    }