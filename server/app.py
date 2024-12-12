from server.api import masterRouter
from .database import setDataBase, create_tables
from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException

#Intialize API
app = FastAPI()

app.include_router(masterRouter, tags=["App Routers"])

#Setup the database on startup
@asynccontextmanager
async def context(app: FastAPI):
    await setDataBase()
    await create_tables()
    yield


#Test router to validate startup
@app.get('/getter')
async def test():
    return {"output": "Start-up validated"}