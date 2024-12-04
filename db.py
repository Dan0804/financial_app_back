from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv("DB_USER")
passwd = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
db = os.getenv("DB_NAME")

db_url = f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{db}"

class engineConn:
    def __init__(self):
        self.engine = create_engine(db_url, pool_recycle=500)

    def sessionMaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connection(self):
        conn = self.engine.connect()
        return conn