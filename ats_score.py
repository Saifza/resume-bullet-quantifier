def ats_score(bullet):
    score = 0

    if len(bullet) > 20:
        score += 3

    if any(word in bullet.lower() for word in [
        "led","built","optimized","designed","created","managed","developed"
    ]):
        score += 3

    if any(char.isdigit() for char in bullet):
        score += 4

    return score