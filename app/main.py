from fastapi import FastAPI
from app.api.v1.chat import router as chat_router

app = FastAPI(
    title="Car Selling Chatbot API",
    version="1.0.0"
)

app.include_router(chat_router, prefix="/api/v1")


@app.get("/")
def health_check():
    return {"status": "Chatbot API running"}
