import stripe
from django.http import JsonResponse
from django.shortcuts import render
from .models import Item, OrderItem
from core.settings.components import config

stripe.api_key = config("STRIPE_SECRET_KEY")


def get_item(request, pk):
    """Displays item info"""
    item = Item.objects.get(pk=pk)
    context = {"item": item, "public_key": config("STRIPE_PUBLIC_KEY")}
    return render(request, "item.html", context=context)


def create_payment_item(request, item_pk):
    """Creates checkout session for an item on Stripe and returns its info in JSON"""
    item = Item.objects.get(pk=item_pk)
    session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": item.name,
                        "description": item.description,
                    },
                    "unit_amount": int(item.price * 100),
                },
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url="http://localhost:8000/success",
        cancel_url="http://localhost:8000/cancel",
    )

    return JsonResponse(session)


def get_order(request, pk):
    """Displays order info"""
    order_items = OrderItem.objects.filter(order__pk=pk)
    context = {"order_items": order_items, "order_id":pk, "public_key": config("STRIPE_PUBLIC_KEY")}
    return render(request, "order.html", context=context)


def create_payment_order(request, order_pk):
    """Creates checkout session for an order on Stripe and returns its info in JSON"""
    order_items = OrderItem.objects.filter(order__pk=order_pk)

    session = stripe.checkout.Session.create(
        line_items=[
            {
                "price_data": {
                    "currency": "usd",
                    "product_data": {
                        "name": order_item.item.name,
                        "description": order_item.item.description,
                    },
                    "unit_amount": int(order_item.item.price * 100),
                },
                "quantity": order_item.amount,
            }
            for order_item in order_items
        ],
        mode="payment",
        success_url="https://" + config("DOMAIN_NAME") + "/success",
        cancel_url="https://" + config("DOMAIN_NAME") + "/cancel",
    )

    return JsonResponse(session)
