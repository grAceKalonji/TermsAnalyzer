from openai import OpenAI
client = OpenAI()
from pypdf import PdfReader


class TermsAnalyzer:
    def __init__(self, pdf_path: str):
        # Parse PDF once, store text as instance variable
        reader = PdfReader(str)
        for page in reader.pages:
            text = page.extract_text()
            
    
    def summarize(text):
        return client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": f"Analyze this legal text and highlight any potentially suspicious clauses that affect user rights, privacy, or hidden costs. Explain simply. {text}"}]
        ).choices[0].message.content
        
    def extract_clauses(text: str) -> str:
        """Pull out individual clauses for finer inspection."""
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": (
                    "Split the following legal text into separate clauses or bullet points "
                    "without changing the wording:\n\n" + text
                )
            }]
        )
        return response.choices[0].message.content
    
    