**What you need to do to make it “submission ready”**
- Plug in a real LLM for rewriting / generation:

- Implement model_client in llm_interface.py using OpenAI or another provider.

- Craft prompts for each section (e.g., “Rewrite this introduction to be more academic, concise, and in APA7 tone…”).

**Enhance search & retrieval:**
- Fetch full-text PDFs if available (use DOI resolvers or arXiv links).

- Extract and summarize abstracts with the LLM.

**Implement or integrate real plagiarism checking:**
- Replace placeholder_external_plagiarism_check with an API call to Turnitin, iThenticate, or other service (requires their enterprise access).

- Optionally, store previously generated drafts to compare for self-plagiarism.

**Improve APA7 formatting:**
- Generate proper title page, abstract formatting, in-text citations, hanging indent references, and optionally export to Word/PDF (use pandoc or python-docx).

**Add citation management:**
- Support BibTeX import/export, DOI resolution, and populate in-text citations automatically.

**Add CLI flags for output types:**
- Allow --format pdf or --format docx by converting the assembled markdown through converters.

**Add tests and validation:**
- Unit tests for each module (search returns results, formatter outputs expected strings, plagiarism thresholds behave).

**-- Run --** 

pip install -r requirements.txt
python journal_writer/run.py "Effects of remote work on productivity" --author "Alice Smith" "Bob Lee" --affiliation "Example University"
