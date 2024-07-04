from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.loader import render_to_string
import requests
from nail_polish_and_currency.models import Types_nail_polish, Variant_nail_polish
from django.http import JsonResponse
from datetime import datetime


def show_nail_polish(request):

    all_types_nail_polish = Types_nail_polish.objects.all()
    all_variant_nail_polish = Variant_nail_polish.objects.all()

    list_id_types = []
    for i in all_variant_nail_polish:
        list_id_types.append(i.types_id)

    list_all_types_nail_polish = {
        'types_nail_polish': all_types_nail_polish,
        'variant_nail_polish': all_variant_nail_polish,
        'all_types_id': list_id_types
    }

    #cursor = create_connection()
    #my_l = []#get_all_robots(cursor)
    #my_p = []#get_all_positions(cursor)
    # all_robots = {
    #     'robots_for_table': my_l,
    #     'positions_for_table': my_p
    # }

    return render(request, 'nail_polish_and_currency/show_nail_polish.html', list_all_types_nail_polish)



def crypto_price_update(request):
    #Получить название монеты и цену первых 20 монет список списков +
    #Передать их в контекст +
    #Создать таблицу с 2 столбцами - название монеты - цена +


    need_symbols = ['BTCUSDT','ETHUSDT','BNBUSDT','XRPUSDT','SOLUSDT','ADAUSDT','DOGEUSDT','TRONUSDT']

    response_by = requests.get('https://api.bybit.com/v5/market/tickers?category=linear')
    result_by = response_by.json()
    my_list_by = result_by['result']['list']

    list_coin_by = []
    for el in my_list_by:
        if el['symbol'] in need_symbols:
            list_coin_by.append((el['symbol'], el["lastPrice"]))


    response_bin = requests.get('https://fapi.binance.com/fapi/v1/ticker/price')
    result_bin = response_bin.json()

    list_coin_bin = []
    for elem in result_bin:
        if elem['symbol'] in need_symbols:
            list_coin_bin.append((elem['symbol'], elem["price"]))

    all_coin = {
        'coin_and_price_bin': sorted(list_coin_bin),
        'coin_and_price_by': list_coin_by,
        'title': 'crypto'
    }
    return render(request, 'nail_polish_and_currency/crypto_price_update.html', all_coin)





def live_broadcast(request):
    need_symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'SOLUSDT', 'ADAUSDT', 'DOGEUSDT', 'TRONUSDT']

    response_by = requests.get('https://api.bybit.com/v5/market/tickers?category=linear')
    result_by = response_by.json()
    my_list_by = result_by['result']['list']

    list_coin_by = []
    for el in my_list_by:
        if el['symbol'] in need_symbols:
            list_coin_by.append((el['symbol'], el["lastPrice"]))

    response_bin = requests.get('https://fapi.binance.com/fapi/v1/ticker/price')
    result_bin = response_bin.json()

    list_coin_bin = []
    for elem in result_bin:
        if elem['symbol'] in need_symbols:
            list_coin_bin.append((elem['symbol'], elem["price"]))


    data = {
        'coin_and_price_bin': sorted(list_coin_bin),
        'coin_and_price_by': list_coin_by,
    }
    return JsonResponse(data)


def post_request(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('exp_date')
        type = request.POST.get('what_type')

        format = "%Y-%m-%d"

        try:
            datetime.strptime(date, format)
        except ValueError:
            return render(request, 'nail_polish_and_currency/request.html',
                          {'title': 'Add nail polish', 'error_message': 'Invalid date format'})

    # Создаем объект модели и сохраняем его в базу данных
        obj = Variant_nail_polish(name=name, expiration_date=date, types_id=type)
        obj.save()

    return render(request, 'nail_polish_and_currency/request.html', {'title': 'Add nail polish'})