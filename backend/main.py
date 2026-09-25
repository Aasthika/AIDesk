from fastapi import FastAPI

app = FastAPI(title="AIDesk API")


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "AIDesk API"}
