from fastapi import FastAPI

from src.views.alive import router as alive_endpoint
from src.views.alert import router as alert_endpoint

from src.impl.config.config import config

app = FastAPI()
app.include_router(alive_endpoint)
app.include_router(alert_endpoint)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.main:app", host=config["host"], port=config["port"], reload=True)