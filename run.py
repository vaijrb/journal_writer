import argparse
import utils
import config
import writer 

def dummy_llm_client(text):
    # Placeholder: in real usage, call OpenAI or other API to improve text.
    # Here, just return the same text.
    return text

def main():
    parser = argparse.ArgumentParser(description="Generate journal article draft.")
    parser.add_argument("topic", help="Research topic")
    parser.add_argument("--author", nargs="+", default=["Vaij Bharamshetty"], help="Author name(s)")
    parser.add_argument("--affiliation", default="N/A", help="Affiliation")
    args = parser.parse_args()

    logger.info(f"Topic: {args.topic}, Author(s): {args.author}, Affiliation: {args.affiliation}")

    result = build_article (args.topic, args.author, args.affiliation, model_client=dummy_llm_client)
    path = save_draft(args.topic, result["article_text"])
    
    print(f"Draft saved to {path}")
    logger.info(f"Draft saved to {path}")
    
    if result["plagiarism"]:
        print("Potential similarity issues found (local check):")
        for issue in result["plagiarism"]:
            print(f"- Score: {issue['score']:.2f}, snippet: {issue['source']}")
    else:
        print("No local similarity issues detected.")

if __name__ == "__main__":

    env = config.get_env_variable()
    logger = config.configure_logging()

    logger.info("Starting article generation process... ")
    
    main()