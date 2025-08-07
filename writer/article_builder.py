import searcher.aggregator
import formatter.apa7
import summarizer.llm_interface
import plagiarism.checker

def build_article(topic, authors, affiliation, model_client=None): #change signature to include model_client
    # 1. Search
    sources = aggregate_search(topic)

    # 2. Generate bibliography entries (APA7)
    references = [format_reference(s) for s in sources]

    # 3. Draft sections (simplified prompts)
    intro = f"This article explores the topic of {topic}. Key prior works include {', '.join([s['title'] for s in sources[:3]])}."
    methods = "Methods: Based on literature review, an exploratory synthesis approach is used."
    results = "Results: The synthesis reveals trends and gaps in current research."
    discussion = "Discussion: Implications of findings, limitations, and future directions."

    # 4. Rewrite/improve sections via LLM if available
    intro = rewrite_section(intro, model_client)
    methods = rewrite_section(methods, model_client)
    results = rewrite_section(results, model_client)
    discussion = rewrite_section(discussion, model_client)

    # 5. Plagiarism check (local)
    similarity_issues = local_similarity_check(intro + methods + results + discussion,
                                              [s.get("abstract", "") for s in sources])

    # 6. Assemble
    title_page = build_title_page(f"Research on {topic}", authors, affiliation)
    article = "\n\n".join([
        title_page,
        "Abstract\n" + f"This article provides a review and synthesis on the topic of {topic}.",
        "Introduction\n" + intro,
        "Methods\n" + methods,
        "Results\n" + results,
        "Discussion\n" + discussion,
        "References\n" + "\n".join(references)
    ])

    return {
        "article_text": article,
        "plagiarism": similarity_issues,
        "sources": sources
    }
