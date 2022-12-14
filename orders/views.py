import json
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import models

from .models import Stock


@csrf_exempt
def place_orders(request):
    if request.method == "POST":
        request_data = json.loads(request.body)
        print(request_data)
        stock = request_data.get("stock", "")
        quantity = request_data.get("quantity", "")
        price = request_data.get("price", "")

        try:
            stock = Stock.objects.get_or_create(
                stock=stock, quantity=quantity, price=price
            )
            return JsonResponse(
                {
                    "id": stock[0].id,
                    "stock": stock[0].stock,
                    "quantity": stock[0].quantity,
                    "price": stock[0].price,
                },
            )
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": ""}, status=400)


def get_total_value(request, id=0):
    if not id:
        stocks = Stock.objects.annotate(
            total_price=models.F("price") * models.F("quantity")
        )
    else:
        stocks = Stock.objects.filter(id=id).annotate(
            total_price=models.F("price") * models.F("quantity")
        )

    total_value = 0
    for stock in stocks:
        total_value += stock.total_price

    return JsonResponse({"total_value": total_value}, status=200)
