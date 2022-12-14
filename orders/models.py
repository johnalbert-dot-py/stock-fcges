from django.db import models

# Create your models here.
class Stock(models.Model):
    id = models.IntegerField(primary_key=True)
    stock = models.CharField(max_length=255, null=True, blank=False)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.stock} | {self.quantity}"
