from django.contrib import admin
from .models import Product

# Register the Product model


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_code', 'price', 'quantity', 'expiry_date', 'admin', 'created_at')
    # Enable search by product name and admin's username
    search_fields = ('product_name', 'admin__username')
    # Add filters by expiry date and creation date
    list_filter = ('expiry_date', 'created_at')
    ordering = ('-created_at',)  # Order by most recently created products
