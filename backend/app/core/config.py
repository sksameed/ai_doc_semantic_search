import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    FAISS_PATH: str = "app/db/faiss_index"

settings = Settings()

if not settings.GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing in .env file")