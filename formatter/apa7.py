from datetime import datetime

def format_author_list(authors):
    if not authors:
        return ""
    if len(authors) == 1:
        return authors[0]
    if len(authors) == 2:
        return f"{authors[0]} & {authors[1]}"
    return ", ".join(authors[:-1]) + f", & {authors[-1]}"

def format_reference(entry):
    # Simplified: assumes crossref/arxiv entry
    authors = format_author_list(entry.get("authors", []))
    title = entry.get("title", "")
    year = ""
    if entry.get("published"):
        try:
            year = datetime.fromisoformat(entry["published"].replace("Z", "+00:00")).year
        except Exception:
            year = entry["published"][:4]
    source = entry.get("source", "")
    doi = entry.get("doi", "")
    if source == "arxiv":
        return f"{authors} ({year}). {title}. arXiv. {doi}"
    else:
        return f"{authors} ({year}). {title}. DOI: {doi}"

def build_title_page(title, authors, affiliation):
    # Very minimal APA7 title page
    lines = []
    lines.append(title)
    lines.append("\n")
    lines.append(format_author_list(authors))
    lines.append("\n")
    lines.append(affiliation)
    return "\n".join(lines)
