from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import ClothingItem
from .forms import ClothingItemForm
from django.conf import settings

def home(request):
    return render(request,'inventory/item_list.html')

def clothing_item_list(request):
    items = ClothingItem.objects.all()
    return render(request, 'inventory/item_list.html', {'items': items})

def clothing_item_create(request):
    if request.method == 'POST':
        form = ClothingItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.current_quantity = item.initial_quantity
            item.save()
            return redirect('item_list')
    else:
        form = ClothingItemForm()
    
    return render(request, 'inventory/item_form.html', {'form': form})
def send_low_stock_alert(item):
    subject = 'Low Stock Alert'
    message = f"The stock for {item.description} ({item.sku}) is below the minimum threshold. Current stock: {item.current_quantity}"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [settings.STORE_MANAGER_EMAIL]  # Replace with the actual manager's email address
    send_mail(subject, message, from_email, recipient_list)
    
def post(self, request):
        form = ClothingItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.current_quantity = item.initial_quantity
            item.save()
            # Check if stock falls below the minimum threshold
            if item.current_quantity < item.min_threshold:
                send_low_stock_alert(item)
