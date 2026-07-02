from groq import Groq
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_content(segment):
    print(f"Generating content for segment {segment['start_time']}s - {segment['end_time']}s...")

    prompt = f"""
    You are a viral social media content creator.
    Based on this video segment:
    - Quote: {segment['quote']}
    - Reason it's viral: {segment['reason']}

    Generate:
    1. viral_headline: A catchy headline
    2. caption: Social media caption with hashtags
    3. summary: 2 sentence summary
    4. broll: B-roll visual description

    Return ONLY a valid JSON object, nothing else.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.choices[0].message.content
    json_match = re.search(r'\{.*\}', raw, re.DOTALL)
    result = json.loads(json_match.group())
    return result
