import requests

def search_crossref(topic, rows=5):
    params = {
        "query.title": topic,
        "rows": rows,
        "sort": "relevance"
    }
    resp = requests.get(env.CROSSREF_ENDPOINT, params=params, timeout=10)
    resp.raise_for_status()
    items = resp.json().get("message", {}).get("items", [])
    results = []
    for item in items:
        results.append({
            "title": item.get("title", [""])[0],
            "authors": [f"{a.get('given','')} {a.get('family','')}".strip() for a in item.get("author", [])] if item.get("author") else [],
            "doi": item.get("DOI"),
            "published": item.get("created", {}).get("date-time"),
            "abstract": item.get("abstract", ""),
            "source": "crossref"
        })
    return results
