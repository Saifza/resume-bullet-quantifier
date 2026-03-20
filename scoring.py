# scoring.py

import re
from config import weak_verbs, strong_verbs, impact_words, passive_words


def action_verb_score(bullet):

    first_word = bullet.split()[0].lower()

    if first_word in strong_verbs:
        return 25

    if first_word in weak_verbs:
        return 5

    return 15


def quantification_score(bullet):

    if re.search(r"\d", bullet):
        return 25

    return 10


def impact_score(bullet):

    text = bullet.lower()

    for word in impact_words:
        if word in text:
            return 25

    return 12


def clarity_score(bullet):

    words = bullet.split()
    length = len(words)

    passive = any(p in bullet.lower() for p in passive_words)

    if not passive and 12 <= length <= 22:
        return 25

    if passive or length > 30:
        return 15

    return 20


def score_bullet(bullet):

    score = (
        action_verb_score(bullet)
        + quantification_score(bullet)
        + impact_score(bullet)
        + clarity_score(bullet)
    )

    return score