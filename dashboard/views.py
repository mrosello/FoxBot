from django.http.response import HttpResponse
from django.shortcuts import render
from dashboard.api_requests import (check_balance, check_all_prices)

def index(request):
    my_balance = check_balance()
    all_prices = check_all_prices()
    data={'my_balance':my_balance, 'all_prices':all_prices}
    return render(request, 'dashboard/index.html', context=data)