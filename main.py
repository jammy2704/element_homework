from fastapi import FastAPI

from app.routers import top_n

app = FastAPI()

app.include_router(top_n.router)
