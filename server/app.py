from server.api import masterRouter
from .database import setDataBase
from fastapi import FastAPI, HTTPException
from server.logging_config import setup_logging


logger = setup_logging()
app = FastAPI()

app.include_router(masterRouter, tags=["App Routers"])

@app.on_event("startup")
async def startEvent():
    try:
        logger.info("Starting database setup...")
        await setDataBase()
        logger.info("Database setup completed successfully.")
    except Exception as e:
        logger.error(f"Error during database setup: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Database setup failed.")

@app.get('/getter')
async def test():
    logger.info("Test route called - Start-up validated.") 
    return {"output": "Start-up validated"}