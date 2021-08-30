from dashboard.api_requests import (check_balance, check_all_prices)

def get_btc_price(asset):
    all_prices = check_all_prices()
    btc_price = 1
    for price in all_prices:
        if price["symbol"] == asset + 'BTC':
            btc_price = float(price["price"])
            break
        if price["symbol"] == 'BTC' + asset:
            btc_price = 1.0/float(price["price"])
    return btc_price

def total_btc_balance():
    my_total_balance = check_balance()
    btc_balance = 0
    for balance in my_total_balance:
        if balance['free'] != '0.00000000' and balance['free'] != '0.00':
            btc_balance = btc_balance + ((float(balance['free'])+float(balance['locked']))*get_btc_price(balance['asset']))
    return btc_balance
 
def pull_wallet():
    return 0