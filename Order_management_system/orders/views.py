from django.shortcuts import render, get_object_or_404, redirect
from .models import Order, FoodItem  # Ensure FoodItem is also imported
from .forms import OrderForm

def index(request):
    orders = Order.objects.prefetch_related('items').all()  # Prefetch items to optimize queries
    return render(request, 'orders/index.html', {'orders': orders})


def add_order(request):
    if request.method == 'POST':
        table_number = request.POST.get('table_number')
        item_names = request.POST.getlist('item_names[]')
        item_prices = request.POST.getlist('item_prices[]')
        status = request.POST.get('status', 'Pending')

        # Debugging: Check if form data is present
        print(f"Table Number: {table_number}, Item Names: {item_names}, Item Prices: {item_prices}, Status: {status}")
        
        if table_number and item_names and item_prices:
            try:
                total_price = sum(float(price) for price in item_prices if price)
                order = Order.objects.create(table_number=table_number, status=status, total_price=total_price)

                # Create order items (ensure your model relationship is correct)
                for name, price in zip(item_names, item_prices):
                    order.items.create(name=name, price=price)

                print(f"Order created with total price: {total_price}")
                
                # Redirect to home (index) after successful submission
                return redirect('index')

            except Exception as e:
                print(f"Error occurred while saving the order: {e}")
                # Optionally, you can render an error message to the user
        else:
            print("Missing required form fields.")
    return render(request, 'orders/add.html')


def edit_order(request, id):
    order = get_object_or_404(Order, id=id)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save()
            item_ids = request.POST.getlist('items[]')  # Get selected items
            order.items.set(FoodItem.objects.filter(id__in=item_ids))  # Update order items
            return redirect('index')
    else:
        form = OrderForm(instance=order)
    
    food_items = FoodItem.objects.all()
    return render(request, 'orders/edit.html', {'form': form, 'order': order, 'food_items': food_items})

def delete_order(request, id):
    order = get_object_or_404(Order, id=id)
    order.delete()
    return redirect('index')

def view_order(request, id):
    order = get_object_or_404(Order, id=id)
    return render(request, 'orders/view_order.html', {'order': order})
