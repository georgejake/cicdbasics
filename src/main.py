from fastapi import FastAPI

app = FastAPI(title="My FastAPI App", version="1.0.0")


@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!", "status": "running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}