from django.shortcuts import render, redirect, get_object_or_404
from .models import Supplier
from .forms import SupplierForm
from django.contrib import messages

# List all suppliers
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_app/supplier_list.html', {'suppliers': suppliers})

# Create a new supplier
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier has been added successfully.")
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    return render(request, 'supplier_app/supplier_form.html', {'form': form})

# Update an existing supplier
def supplier_update(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplier has been updated successfully.")
            return redirect('supplier_list')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'supplier_app/supplier_form.html', {'form': form, 'supplier': supplier})

# Delete an existing supplier
def supplier_delete(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        supplier.delete()
        messages.success(request, "Supplier has been deleted successfully.")
        return redirect('supplier_list')
    return render(request, 'supplier_app/supplier_confirm_delete.html', {'supplier': supplier})