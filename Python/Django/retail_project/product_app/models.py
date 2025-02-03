from django.db import models
from supplier_app.models import Supplier  # Importing Supplier model

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=200)
    Description = models.TextField(blank=True, null=True)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    StockQuantity = models.PositiveIntegerField()
    Suppliers = models.ManyToManyField(Supplier, related_name="products")  # Many-to-Many relationship

    def __str__(self):
        return self.Name
