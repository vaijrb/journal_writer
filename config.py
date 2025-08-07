import os

model_client = None # Placeholder for LLM client, e.g., OpenAI

def get_env_variable():
    # API keys (set via environment variables or override here)
    CROSSREF_ENDPOINT = "https://api.crossref.org/works"
    ARXIV_API_URL = "http://export.arxiv.org/api/query"

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    # Placeholder for plagiarism service, e.g., Turnitin
    PLAGIARISM_API_KEY = os.getenv("PLAGIARISM_API_KEY", "")

    # Thresholds
    PLAGIARISM_LOCAL_SIMILARITY_THRESHOLD = 0.7  # for fuzzy matching
    MAX_SEARCH_RESULTS = 5

    return {
        "CROSSREF_ENDPOINT": CROSSREF_ENDPOINT,
        "ARXIV_API_URL": ARXIV_API_URL,
        "OPENAI_API_KEY": OPENAI_API_KEY,
        "PLAGIARISM_API_KEY": PLAGIARISM_API_KEY,
        "PLAGIARISM_LOCAL_SIMILARITY_THRESHOLD": PLAGIARISM_LOCAL_SIMILARITY_THRESHOLD,
        "MAX_SEARCH_RESULTS": MAX_SEARCH_RESULTS
    }

def configure_logging():
    import logging
    from logging.handlers import RotatingFileHandler

    # Create a logger
    logger = logging.getLogger("article_writer")
    logger.setLevel(logging.INFO)

    # Create a file handler with rotation
    handler = RotatingFileHandler("output/logs/articleWriter.log", maxBytes=10**6, backupCount=5)
    handler.setLevel(logging.INFO)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    
    return logger    