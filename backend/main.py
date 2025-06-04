from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": f"Hello from FastAPI! ENV={os.getenv('APP_ENV')}"}
