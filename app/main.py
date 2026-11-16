from fastapi import FastAPI

app = FastAPI(title="Docker DevOps Lab")


@app.get("/")
def root():
    return {"message": "Hello from my Docker CI/CD project!"}


@app.get("/health")
def health():
    return {"status": "ok"}
