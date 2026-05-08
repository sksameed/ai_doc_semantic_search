import os
from langchain_community.vectorstores import FAISS
from app.core.config import settings


class VectorService:

    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.db_path = settings.FAISS_PATH

    def store(self, chunks):

        index_file = os.path.join(self.db_path, "index.faiss")
        pkl_file = os.path.join(self.db_path, "index.pkl")

        # Load existing DB only if BOTH files exist
        if os.path.exists(index_file) and os.path.exists(pkl_file):

            db = FAISS.load_local(
                self.db_path,
                self.embeddings,
                allow_dangerous_deserialization=True
            )

            db.add_documents(chunks)

        else:
            db = FAISS.from_documents(chunks, self.embeddings)

        db.save_local(self.db_path)

    def retrieve(self, query: str, k: int = 3):

        index_file = os.path.join(self.db_path, "index.faiss")
        pkl_file = os.path.join(self.db_path, "index.pkl")

        if not os.path.exists(index_file) or not os.path.exists(pkl_file):
            raise Exception("No indexed documents found")

        db = FAISS.load_local(
            self.db_path,
            self.embeddings,
            allow_dangerous_deserialization=True
        )

        return db.similarity_search(query, k=k)