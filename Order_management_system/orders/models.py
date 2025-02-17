from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    table_number = models.IntegerField()
    items = models.ManyToManyField(FoodItem)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('ready', 'Ready'), ('paid', 'Paid')], default='pending')

    def total_price(self):
        return sum(item.price for item in self.items.all())  # Sum up all item prices
    def __str__(self):
        return f"Table {self.table_number} - {self.status}"
