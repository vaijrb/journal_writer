# This is a pluggable interface. Plug in OpenAI or other LLM here.

def rewrite_section(prompt_text, model_client=None):
    """
    Given section text, send to LLM for improvement / paraphrasing.
    model_client is expected to be a callable interface; you can adapt to OpenAI, etc.
    """
    if model_client is None:
        # naive fallback: return original
        return prompt_text
    return model_client(prompt_text)
