from os import environ
from dotenv import load_dotenv
load_dotenv()

envapi = environ.get("API_KEY")
API_KEY = envapi if envapi is not None  else input("Binance API key please: ")
envsecret = environ.get("API_SECRET")
API_SECRET = envsecret if envsecret is not None  else input("Binance API Secret please: ")