from server.api import masterRouter
from .database import setDataBase, create_tables
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from server.logging_config import setup_logging


logger = setup_logging()
app = FastAPI()

app.include_router(masterRouter, tags=["App Routers"])

#Setup the database on startup
@asynccontextmanager
async def context(app: FastAPI):
    await setDataBase()
    logger.info("Database setup completed successfully.")
    await create_tables()
    yield


#Test router to validate startup
@app.get('/getter')
async def test():
    logger.info("Test route called - Start-up validated.") 
    return {"output": "Start-up validated"}