from fuzzywuzzy import fuzz
from config import PLAGIARISM_LOCAL_SIMILARITY_THRESHOLD

def local_similarity_check(generated_text, source_texts):
    """
    Compare generated_text against a list of source_texts. Returns list of
    tuples (source_snippet, similarity_score) over threshold.
    """
    issues = []
    for src in source_texts:
        score = fuzz.partial_ratio(generated_text.lower(), src.lower()) / 100.0
        if score >= PLAGIARISM_LOCAL_SIMILARITY_THRESHOLD:
            issues.append({
                "source": src[:200] + ("..." if len(src) > 200 else ""),
                "score": score
            })
    return issues

def placeholder_external_plagiarism_check(text):
    """
    Stub for external plagiarism service (e.g., Turnitin API).
    You'd implement an HTTP client here to send `text` and parse response.
    """
    # Raise NotImplemented or return mock
    return {"status": "not_implemented", "matches": []}
