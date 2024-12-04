from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from db import engineConn
from models import Test

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

engine = engineConn()
session = engine.sessionMaker()

class Item(BaseModel):
    name: str
    email: str

@app.get("/")
async def first_get():
    example = session.query(Test).all()
    return example