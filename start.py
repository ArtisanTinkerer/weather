
# connect to weather API
# save to db
import requests
from dotenv import load_dotenv
import os


load_dotenv()
url = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'


if __name__ == "__main__":
   lat = 53.1038208
   long = -2.1692416
   key=os.getenv('KEY')
   url = url.format(lat=lat, lon=long, API_key=key)
   response = requests.get(url)
   data = response.json()
   print(data)
   # save to db
   # SQL Alchemy
   # connect to db
