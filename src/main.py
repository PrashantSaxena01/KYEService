import os
from dotenv import load_dotenv
import uvicorn

# Load environment early so defaults are applied when FastAPI starts
load_dotenv()


def run() -> None:
    """Start the Uvicorn server."""
    host = os.getenv("APP_HOST", "0.0.0.0")
    port = int(os.getenv("APP_PORT", "8000"))
    uvicorn.run("src.api.fastapi_app:app", host=host, port=port, reload=True)


if __name__ == "__main__":
    run()
