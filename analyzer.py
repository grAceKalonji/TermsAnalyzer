from openai import OpenAI
client = OpenAI()

def summarize(text):
    return client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Analyze this legal text and highlight any potentially suspicious clauses that affect user rights, privacy, or hidden costs. Explain simply. {text}"}]
    ).choices[0].message.content