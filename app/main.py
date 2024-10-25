from fastapi import FastAPI

from .routers import hr_attritions_router

app = FastAPI()

app.include_router(hr_attritions_router.router)


@app.get("/")
async def root():
    return {"message": "Hello Data Science Application!"}
