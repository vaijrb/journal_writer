import requests
import xml.etree.ElementTree as ET
import ARXIV_API_URL

def search_arxiv(topic, max_results=5):
    query = f"search_query=all:{topic}&start=0&max_results={max_results}"
    url = f"{ARXIV_API_URL}?{query}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    root = ET.fromstring(resp.text)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    entries = []
    for entry in root.findall('atom:entry', ns):
        title = entry.find('atom:title', ns).text.strip()
        summary = entry.find('atom:summary', ns).text.strip()
        authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)]
        published = entry.find('atom:published', ns).text
        entries.append({
            "title": title,
            "authors": authors,
            "doi": entry.find('atom:id', ns).text,
            "published": published,
            "abstract": summary,
            "source": "arxiv"
        })
    return entries
