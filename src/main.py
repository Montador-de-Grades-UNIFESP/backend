from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv('CORS_ORIGINS', ['http://localhost:5173']),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from api import router as api_router

app.include_router(api_router)

@app.get("/ping")
async def pong():
    return {"ping": "pong!"}
