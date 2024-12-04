from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class Test(base):
    __tablename__ = "test"

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)