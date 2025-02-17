# The commented out code block is attempting to register the `Order` model with the Django admin site.
# However, it seems like the code is commented out using `#`, which means it is not currently active
# or being executed. If you want to register the `Order` model with the admin site, you can uncomment
# this code block by removing the `#` symbols at the beginning of each line.
from django.contrib import admin
from .models import Order

# Register your models here.
admin.site.register(Order)

