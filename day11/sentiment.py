from groq import Groq
import os
from dotenv import load_dotenv
#from sentence_transformers import SentenceTransformer
#from sentence_transformers import util


load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)
prompt = """
Classify the sentiment of the following texts.

Examples:
Text: "I love this product" → {"sentiment": "positive", "confidence": "high"}
Text: "This is terrible" → {"sentiment": "negative", "confidence": "high"}
Text: "It's okay I guess" → {"sentiment": "neutral", "confidence": "medium"}

Now classify this text and respond in JSON only:
Text: "I really enjoyed learning Python today"
"""

response = client.chat.completions.create(model="llama-3.3-70b-versatile", messages=[
    {"role": "system", "content": "You are a sentiment classifier. Respond in JSON only."},
    {"role": "user", "content": prompt}
]
)
print(response.choices[0].message.content)
"""
model = SentenceTransformer("all-MiniLM-L6-v2")

embedding1 = model.encode("I love machine learning")
embedding2 = model.encode("I enjoy deep learning")



similarity = util.cos_sim(embedding1, embedding2)
print(similarity) """

