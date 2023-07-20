from fastapi import FastAPI

from controller import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    """
    Entry point of the collector application.
    Starts the API behind uvicorn.
    """
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
