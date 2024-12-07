from server.api import masterRouter
from .database import setDataBase
from fastapi import FastAPI, HTTPException

#Intialize API
app = FastAPI()

app.include_router(masterRouter, tags=["App Routers"])

#Setup the database on startup
@app.on_event("startup")
async def startEvent():
    await setDataBase()
    

#Test router to validate startup
@app.get('/getter')
async def test():
    return {"output": "Start-up validated"}