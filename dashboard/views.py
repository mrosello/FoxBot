from django.shortcuts import render
from dashboard.api_requests import (check_balance, check_pair_price)
from dashboard.utils import (total_btc_balance)

def index(request):
    my_balance = check_balance()
    my_total_btc_balance = round(total_btc_balance(), 5)
    BTC_to_EUR = check_pair_price("BTCEUR")
    my_total_eur_balance = round(my_total_btc_balance * float(BTC_to_EUR),2)
    BTC_to_USD = check_pair_price("BTCUSDT")
    my_total_usd_balance = round(my_total_btc_balance * float(BTC_to_USD),2)

    my_total_eur_balance = round(my_total_btc_balance * float(BTC_to_EUR),2)
    data={'my_balance':my_balance, 'my_total_btc_balance':my_total_btc_balance, 'my_total_eur_balance':my_total_eur_balance, 'my_total_usd_balance':my_total_usd_balance}
    return render(request, 'dashboard/index.html', context=data)