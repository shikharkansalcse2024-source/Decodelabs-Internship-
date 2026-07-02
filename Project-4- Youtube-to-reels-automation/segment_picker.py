from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def pick_viral_segments(transcript_text):
    print("Finding viral segments...")

    prompt = f"""
    You are a social media expert. Read this transcript and find 5 most viral segments.
    For each segment return:
    - start_time (in seconds, as integer)
    - end_time (in seconds, as integer)
    - reason (why it's viral)
    - quote (exact words from segment)

    Return ONLY a valid JSON array, nothing else.

    Transcript:
    {transcript_text}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    result = json.loads(response.choices[0].message.content)
    print("Segments found!")
    return result
