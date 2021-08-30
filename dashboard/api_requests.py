from binance.client import Client
from binance.exceptions import BinanceAPIException
from requests.exceptions import ReadTimeout, ConnectionError
import config

client = Client(config.API_KEY, config.API_SECRET)

def check_balance():
    """ found balances available for the client """
    try:
        balance = client.get_account(recvWindow=59000)['balances']
    except ReadTimeout:
        balance = "ReadTimeout during check balance"
    except ConnectionError:
        balance = "ConnectionError during check balance"
    except BinanceAPIException as e:
        print(e.status_code)
        print(e.message)
        balance = "BinanceAPIException during check balance"
    return balance

def check_all_prices():
    """ getting all pair prices"""
    prices = client.get_all_tickers()
    return prices

def check_pair_price(pair):
    """ checking a pair price"""
    price = client.get_avg_price(symbol=pair)["price"]
    return price