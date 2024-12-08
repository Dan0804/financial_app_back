from pydantic import BaseModel, Field
from datetime import datetime

class UserForAdmin(BaseModel):
    _id: int
    email: str
    password : str
    date: datetime = Field(description="it's defined when register user data", examples="2024-12-08")
    auth: str = Field(description="it has two auth category(admin and customer)", examples="customer")

    class Config:
        orm_mode = True

class User(BaseModel):
    email: str
    password:str

    class Config:
        orm_mode = True