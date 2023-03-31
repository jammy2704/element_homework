from fastapi import FastAPI
from app.routers import topN


app = FastAPI()

app.include_router(topN.router)
