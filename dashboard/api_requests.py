from binance.client import Client
from binance.exceptions import BinanceAPIException
from requests.exceptions import ReadTimeout, ConnectionError
import config

def check_balance():
    """ found balances available for the client """
    try:
        balance = Client(config.API_KEY, config.API_SECRET).get_account()['balances']
    except ReadTimeout:
        balance = "ReadTimeout during check balance"
    except ConnectionError:
        balance = "ConnectionError during check balance"
    except BinanceAPIException:
        balance = "BinanceAPIException during check balance"
    return balance