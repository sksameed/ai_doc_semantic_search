from langchain_community.vectorstores import FAISS

DB_PATH = "app/db/faiss_index"

def save_to_faiss(chunks, embeddings):
    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(DB_PATH)

def load_faiss(embeddings):
    return FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )