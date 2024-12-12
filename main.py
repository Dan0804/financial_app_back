from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from db import engineConn
from models import Users
from schema.users import User

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

@app.post("/login/", response_model=User)
async def login(user: User):
    data = session.query(Users).filter(Users.email == user.email, Users.password == user.password).first()
    
    if data is not None:
        return data
        
    raise HTTPException(status_code=404, detail="Please check the e-mail or password")