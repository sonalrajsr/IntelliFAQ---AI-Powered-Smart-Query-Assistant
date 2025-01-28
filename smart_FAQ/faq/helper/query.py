from groq import Groq
from dotenv import load_dotenv
import os 

load_dotenv()

def query_serpapi(query):
    client = Groq(
        api_key=os.environ.get('GORQ_API'),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    return chat_completion.choices[0].message.content

print(query_serpapi('Tell me in sort about the privacy policy about making youtube channel'))