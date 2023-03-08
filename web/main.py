import uvicorn
from cmd.send import Methods

if __name__ == "__main__":
    uvicorn.run(
        app="studio.app:fastapi_app",
        host="127.0.0.1",
        port=8000,
        reload=True,
        log_level="debug",
    )
