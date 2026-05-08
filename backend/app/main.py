from fastapi import FastAPI
from app.api import upload, chat, health

app = FastAPI()

app.include_router(upload.router)
app.include_router(chat.router)
app.include_router(health.router)

@app.get("/")
def root():
    return {"message": "API running"}