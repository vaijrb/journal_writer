import crossref_search
import arxiv_search
import semantic_scholar_search  # TODO: Implement this function

def aggregate_search(topic, max_per_source=3):
    results = []
    results.extend(search_crossref(topic, rows=max_per_source))
    results.extend(search_arxiv(topic, max_results=max_per_source))
    # Uncomment the next line when implemented
    # results.extend(search_semantic_scholar(topic, max_results=max_per_source))
    # Deduplicate based on title
    seen = set()
    unique = []
    for r in results:
        title = r.get("title", "")
        key = title.lower()
        if not title or key in seen:
            continue
        seen.add(key)
        unique.append(r)
    return unique