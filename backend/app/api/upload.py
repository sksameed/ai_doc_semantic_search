from fastapi import APIRouter, UploadFile, File
import os

from app.services.pdf_service import load_pdf
from app.services.chunk_service import split_docs
from app.services.embedding_service import get_embeddings
from app.services.vector_service import VectorService

router = APIRouter()

UPLOAD_DIR = "app/data"

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    try:
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        print("PDF SAVED")

        docs = load_pdf(file_path)

        print("PDF LOADED")

        chunks = split_docs(docs)

        print("CHUNKS CREATED:", len(chunks))

        embeddings = get_embeddings()

        print("EMBEDDINGS LOADED")

        vector_service = VectorService(embeddings)

        vector_service.store(chunks)

        print("VECTOR STORED")

        return {
            "message": "File processed successfully",
            "chunks": len(chunks)
        }

    except Exception as e:
        print("UPLOAD ERROR:", str(e))
        return {"error": str(e)}