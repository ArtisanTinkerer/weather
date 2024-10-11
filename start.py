
# connect to weather API
# save to db
import requests
from dotenv import load_dotenv
import os

from requests import session
from sqlalchemy import create_engine
from sqlalchemy import text
from current import Current
from sqlalchemy.orm import sessionmaker
from base import Session, engine, Base





url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'


if __name__ == "__main__":
   load_dotenv()
   username = os.getenv('DB_USERNAME')
   password = os.getenv('DB_PASSWORD')
   #engine = create_engine(f'postgresql+psycopg2://{username}:{password}@localhost/weather')

   session = Session()

   new_current = Current("London", "hot")
   session.add(new_current)
   session.commit()
   session.close()



   lat = 53.1038208
   long = -2.1692416
   key=os.getenv('KEY')
   url = url.format(lat=lat, lon=long, API_key=key)
   response = requests.get(url)
   data = response.json()
   print(data)
   # save to db
   # Alembic for migrations
   # SQL Alchemy
   # Migration to create a table - with date and time
   # Baro pressure to see trend?
   # goals
   # - create Table with Alembic
   # - create Model and populate 1 row

   #query the db
   #

