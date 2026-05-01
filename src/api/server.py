from fastapi import FastAPI

app = FastAPI(
    title="Movie Manager API",
    summary="Backend API for tracking users and their saved movies.",
    version="0.1.0",
)


@app.get("/", tags=["meta"])
def read_root() -> dict[str, str]:
    return {
        "service": "movieManager",
        "status": "ok",
        "docs": "/docs",
    }


@app.get("/health", tags=["meta"])
def read_health() -> dict[str, str]:
    return {"status": "healthy"}
