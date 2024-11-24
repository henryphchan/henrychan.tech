from django.db import models

# Create your models here.
from django.db import models

class Supplier(models.Model):
    ACTIVE_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    ]

    SupplierID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    ContactPerson = models.CharField(max_length=100)
    ContactEmail = models.EmailField(max_length=100, blank=True, null=True)
    PhoneNumber = models.CharField(max_length=20, blank=True, null=True)
    Address = models.TextField(blank=True, null=True)
    ActiveStatus = models.CharField(max_length=8, choices=ACTIVE_STATUS_CHOICES)
    ContractStartDate = models.DateField(blank=True, null=True)
    ContractEndDate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.Name