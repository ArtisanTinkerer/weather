from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()
username =  os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')

engine = create_engine(f'postgresql+psycopg2://{username}:{password}@localhost/weather')
Session = sessionmaker(bind=engine)

Base = declarative_base()