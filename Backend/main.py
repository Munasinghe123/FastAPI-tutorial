from fastapi import FastAPI
from database import engine,Base
from routes.user_routes import router as use_router


app= FastAPI(title="first project")

Base.metadata.create_all(bind=engine)

app.include_router(use_router)

@app.get("/")
def health():
    return{"status":"running"}