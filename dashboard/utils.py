from dashboard.api_requests import (check_balance, check_pair_price, check_all_prices)

def get_btc_price(asset):
    btc_price = 0
    if asset == 'BTC':
        btc_price = 1
    elif asset == 'EUR':
        btc_price = 1.0/float(check_pair_price('BTC' + asset))
    else:
        btc_price = float(check_pair_price(asset + 'BTC'))
    return btc_price

def total_btc_balance():
    my_total_balance = check_balance()
    btc_balance = 0
    for balance in my_total_balance:
        if balance['free'] != '0.00000000' and balance['free'] != '0.00':
            btc_balance = btc_balance + ((float(balance['free'])+float(balance['locked']))*get_btc_price(balance['asset']))
    return btc_balance