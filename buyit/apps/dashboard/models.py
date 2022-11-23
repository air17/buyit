from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Order(models.Model):
    def __str__(self):
        return "Order #" + str(self.id)


class Item(models.Model):
    name = models.CharField("Name", max_length=255)
    description = models.TextField("Description")
    price = models.DecimalField(
        "Price",
        decimal_places=2,
        max_digits=15,
        validators=[MinValueValidator(Decimal(0.0))],
    )

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    item = models.ForeignKey(Item, models.CASCADE)
    amount = models.PositiveIntegerField(
        "Item amount in an order",
        default=1,
        validators=[MinValueValidator(1)],
    )
    order = models.ForeignKey(Order, models.CASCADE)

    def __str__(self):
        return f"{self.amount} {self.item}s in {self.order}"
