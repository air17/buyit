from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("item/<int:pk>", views.get_item, name="item"),
    path("buy/<int:item_pk>", views.create_payment_item, name="buy"),
    path("order/<int:pk>", views.get_order, name="order"),
    path("buy-order/<int:order_pk>", views.create_payment_order, name="buy-order"),
]
