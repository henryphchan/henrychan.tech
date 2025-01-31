from django.db import models

class Supplier(models.Model):
    ACTIVE_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive')
    ]

    SupplierID = models.AutoField(primary_key=True) # Automatically generated unique ID for each supplier.
    Name = models.CharField(max_length=100) # Stores supplier names as strings (up to 100 characters).
    ContactPerson = models.CharField(max_length=100) # Stores the supplier's contact person.
    ContactEmail = models.EmailField(max_length=100, blank=True, null=True) # Stores an optional email with email validation.
    PhoneNumber = models.CharField(max_length=20, blank=True, null=True) # Stores an optional phone number.
    Address = models.TextField(blank=True, null=True) # Stores an optional address.
    ActiveStatus = models.CharField(max_length=8, choices=ACTIVE_STATUS_CHOICES) # Dropdown with "Active" or "Inactive" options.
    ContractStartDate = models.DateField(blank=True, null=True) # Stores an optional contract start date.
    ContractEndDate = models.DateField(blank=True, null=True) # Stores an optional contract end date.

    """
    This method ensures that when a Supplier object is printed or displayed, its Name will be shown instead of the default object representation.
    """
    def __str__(self):
        return self.Name