from groq import Groq
from app.core.config import settings
from app.services.embedding_service import get_embeddings
from app.services.vector_service import VectorService

# Validate API key early
if not settings.GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in environment variables")

client = Groq(api_key=settings.GROQ_API_KEY)

def ask_question(query: str):
    embeddings = get_embeddings()
    vector_service = VectorService(embeddings)

    try:
        docs = vector_service.retrieve(query, k=3)
    except Exception as e:
        return {"error": str(e)}

    context = "\n\n".join([doc.page_content for doc in docs])
    sources = [doc.metadata.get("page", "unknown") for doc in docs]

    prompt = f"""
You are a helpful assistant. Answer ONLY using the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    answer = response.choices[0].message.content

    return {
        "answer": answer,
        "sources": sources
    }