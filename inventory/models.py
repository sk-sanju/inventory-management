from django.db import models

class ClothingItem(models.Model):
    sku = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=255)
    supplier = models.CharField(max_length=255)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    initial_quantity = models.PositiveIntegerField()
    current_quantity = models.PositiveIntegerField()
    min_threshold = models.PositiveIntegerField(default=10)

    def __str__(self):
        return f"{self.sku} - {self.description}"

