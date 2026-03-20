# scorecard.py

def generate_scorecard(results, bullets, match_score=None):
    """
    Generate overall resume score and breakdown
    """

    total_score = sum([r["score"] for r in results]) / len(results)

    weak_verbs_count = sum([1 for r in results if r["weak_verbs"]])
    generic_count = sum([1 for r in results if r["generic_phrases"]])

    # bullets without numbers (very simple heuristic)
    no_metrics = sum([1 for b in bullets if not any(char.isdigit() for char in b)])

    # final score (weighted)
    final_score = total_score

    if match_score:
        final_score = (0.7 * total_score) + (0.3 * match_score)

    return {
        "final_score": round(final_score, 1),
        "avg_score": round(total_score, 1),
        "weak_verbs": weak_verbs_count,
        "generic_phrases": generic_count,
        "no_metrics": no_metrics
    }