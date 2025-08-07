# from s2_folks.api import SemanticScholarAPI
# from s2_folks.processing import paper_text_summary

# Initialize the API client
api = SemanticScholarAPI()

# Step 1: Search for papers on a given topic
# query = "AI governance and ethical frameworks"
results = api.search_papers(query=query, limit=5)

# Step 2: Retrieve paper details and summarize
summaries = []

for paper in results:
    paper_id = paper.get("paperId")
    title = paper.get("title")
    url = paper.get("url")
    
    logger.info(f"Fetching: {title}")
    paper_details = api.get_paper(paper_id)

    # Basic summary generation using abstract
    abstract = paper_details.get("abstract", "")
    summary = paper_text_summary(abstract) if abstract else "No abstract available."

    summaries.append({
        "title": title,
        "summary": summary,
        "link": url
    })

# Step 3: Display the gathered summaries
for item in summaries:
    print(f"\nTitle: {item['title']}")
    print(f"Summary: {item['summary']}")
    print(f"Link: {item['link']}")