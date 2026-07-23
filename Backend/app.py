from fastapi import FastAPI

from api.routes import router
from database.db import init_db
app = FastAPI(
    title="HR Multi-Agent Backend"
)


app.include_router(router)


@app.get("/")
def root():

    return {
        "message": "HR Backend Running"
    }

init_db()