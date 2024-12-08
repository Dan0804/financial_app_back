from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Users(base):
    __tablename__ = "user_table"

    _id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    email = Column(String(40), nullable=False)
    password = Column(String(255), nullable=False)
    created_date = Column(Date, nullable=False)
    auth = Column(String(8), nullable=False, default="customer")