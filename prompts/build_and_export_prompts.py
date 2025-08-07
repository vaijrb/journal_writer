import textwrap
import json

def get_prompt_template(section, topic, context):
    """
    Returns a filled-in prompt string for the specified section.
    Also returns a dictionary representation of the prompt for JSON export.
    """
    authors = ", ".join(context.get("author_list", ["John Doe"]))
    affiliation = context.get("affiliations", "University X")
    journal = context.get("journal_name", "[Journal Name]")
    gap = context.get("research_gap", "")
    objectives = context.get("objectives_or_hypotheses", "")
    findings = context.get("summary", "")
    keywords = context.get("keywords", "")
    background_sources = context.get("background_sources", [])

    """
    # Templates for each section of the article draft.
    # Title
        Instructions:
            Generate an APA 7th edition title page. Include:
            - Full title (concise, descriptive, max 15 words)
            - Author names and affiliations
            - Author note if applicable (funding, contact info)
            - Running head (if required)
        Provide 2 alternate title suggestions (<=15 words).
    # Abstract
        Instructions:
            Write an APA7 abstract (~200 words) with:
            - Background
            - Objective
            - Methods
            - Key results
            - Conclusion
            Add "Keywords:" with 4-6 terms.
        Use academic tone, include citation placeholders like (Smith & Lee, 2020) if needed.
    # Introduction
        Instructions:
            Write an APA7 Introduction (~700 words) with:
            - Area introduction and importance
            - Summary of prior work (2-3 themes)
            - Research gap
            - Study objective/questions
            - Significance
        Use in-text citation placeholders. Maintain academic tone.
    # Methods
        Instructions:
            Write an APA7 Methods section (~1000 words) with:
            - Participants (sample size, demographics)
            - Measures (instruments, scales)
            - Procedure (study design, data collection)
            - Analysis (statistical methods)
        Use past tense, APA7 tone. Include citation placeholders.
    # Results
        Instructions:
            Write an APA7 Results section (~1000 words) with:   
    # Discussion    
        Instructions:
            Write an APA7 Discussion section (~1000 words) with:
            - Summary of findings
            - Comparison to prior work
            - Theoretical/practical implications
            - Limitations
            - Future directions
            - Final takeaway
        Use in-text citation placeholders. Maintain academic tone.
    # Conclusion
        Instructions:
            Write an APA7 Conclusion (~200 words) summarizing:
            - Contribution of study
            - Most important findings
            - Final recommendation or implication
        Use academic tone, no new information.
    # References
        Instructions:
            Format the provided sources into APA7 References section.
            Use hanging indent format. List alphabetically by first author surname.
    """
    templates = {
        "title_page": f"""
            Topic: {topic}
            Authors: {authors}
            Affiliations: {affiliation}
            Target journal: {journal}            
        """,
        "abstract": f"""
            Topic: {topic}
            Summary bullets: {findings}
       """,
        "introduction": f"""
            Topic: {topic}
            Research gap: {gap}
            Objectives: {objectives}
            Background sources: {background_sources}
         """,
        "methods": f"""
            Topic: {topic}
            Study design: {context.get('design_description', '')}
            Sample: {context.get('sample_description', '')}
            Measures: {context.get('measures_list', '')}
            Procedure: {context.get('procedure_summary', '')}
            Analysis: {context.get('analysis_methods', '')}       
        """,
        "results": f"""
            Topic: {topic}
            Key findings: {findings}         
        """,
        "discussion": f"""
            Topic: {topic}
            Summary: {findings}
            Research gap: {gap}
            Objectives: {objectives}
            Implications: {context.get('implications', '')}
            Limitations: {context.get('known_limitations', '')}
        """,
        "conclusion": f"""
            Topic: {topic}
            Key takeaways: {findings}            
        """,
        "references": f"""
            Topic: {topic}
            Sources: {background_sources}
        """
    }

    prompt = templates.get(section, f"Section '{section}' not recognized.")
    prompt = textwrap.dedent(prompt)

    return {
        "section": section,
        "prompt": prompt.strip(),
        "topic": topic,
        "context": context
    }

def export_prompts_to_json(sections, topic, context, output_path):
    prompts = [get_prompt_template(section, topic, context) for section in sections]
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(prompts, f, indent=2, ensure_ascii=False)
    return output_path
