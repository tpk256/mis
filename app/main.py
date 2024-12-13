from fastapi import FastAPI
from views.api import router

app = FastAPI()

app.include_router(router)