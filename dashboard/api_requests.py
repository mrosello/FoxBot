from binance.client import Client
from binance.exceptions import BinanceAPIException
from requests.exceptions import ReadTimeout, ConnectionError
import config

def check_balance():
    """ found balances available for the client """
    try:
        balance = Client(config.API_KEY, config.API_SECRET).get_account(recvWindow=59000)['balances']
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
    """ for conversion purpose, convert btc to usd"""
    prices = Client(config.API_KEY, config.API_SECRET).get_all_tickers()
    return prices