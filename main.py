from fastapi import FastAPI

from app import routes

app = FastAPI()


for router in routes:
    app.include_router(router)
