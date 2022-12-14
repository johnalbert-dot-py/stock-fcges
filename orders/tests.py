from django.test import TestCase
from django.db import models
from .models import Stock

# Create your tests here.


class StockTestCase(TestCase):
    def setUp(self):
        Stock.objects.create(stock="Test Stock", price=100.00, quantity=1)
        Stock.objects.create(stock="Test Stock 2", price=200.00, quantity=2)
        Stock.objects.create(stock="Test Stock 3", price=300.00, quantity=3)

    def test_total_value(self):
        test_stocks = Stock.objects.annotate(
            total_price=models.F("price") * models.F("quantity")
        )

        total_value = 0
        for stock in test_stocks:
            total_value += stock.total_price

        self.assertEqual(total_value, 1400)
