def academic_section_llm(topic, section, context, model_client):
    prompt = build_prompt_for_section(section, topic, context)  # implement mapping above
    response = model_client([
        {"role": "system", "content": SYSTEM_INSTRUCTIONS},
        {"role": "user", "content": prompt}
    ], temperature=0.2, max_tokens=1200)
    return response  # extract .choices[0].message.content depending on SDK
