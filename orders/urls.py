from django.urls import path
from .views import place_orders, get_total_value

urlpatterns = [
    path("", place_orders, name="place-orders"),
    path("total/", get_total_value, name="get-total-value"),
]
