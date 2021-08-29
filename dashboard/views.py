from django.http.response import HttpResponse
from django.shortcuts import render
from dashboard.api_requests import (check_balance)

def index(request):
    my_balance = check_balance()
    data={'my_balance':my_balance}
    return render(request, 'dashboard/index.html', context=data)