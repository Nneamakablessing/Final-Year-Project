
from PIL import Image
# from pyzbar.pyzbar import decode
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.core.files.storage import FileSystemStorage
import requests
from .forms import ProductRegistrationForm
import datetime
from django.contrib import messages  # For flash messages
from django.utils import timezone
from datetime import timedelta  # Add this line to import timedelta



# Create your views here.
def dashboard_views(request):
    # Get today's date
    today = timezone.now().date()

    # Query expired products
    expired_products = Product.objects.filter(expiry_date__lt=today)

    # Query products expiring within the next 14 days
    soon_to_expire_date = today + timedelta(days=14)
    expiring_soon_products = Product.objects.filter(expiry_date__gte=today, expiry_date__lte=soon_to_expire_date)

    # Count expired and non-expired products
    expired_count = Product.objects.filter(expiry_date__lt=today).count()
    not_expired_count = Product.objects.filter(expiry_date__gte=today).count()
    soon_to_expire_date = today + timedelta(days=14)
    expiring_soon_count = Product.objects.filter(
        expiry_date__lte=soon_to_expire_date, expiry_date__gte=today).count()


    context = {
        'expired_products': expired_products,  # Already expired products
        'expiring_soon_products': expiring_soon_products,  # Products expiring within 14 days
        'expired_count': expired_count,  # Count of expired products
        'not_expired_count': not_expired_count,  # Count of not expired products
        'expiring_soon_count': expiring_soon_count
    }

    return render(request, 'admin/home.html', context)

def products_views(request):
    products = Product.objects.all()  # Fetch all products from the database
    # Pass products to the template
    return render(request, 'admin/products.html', {'products': products})

def delete_product(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id') or request.GET.get('product_id')
        job = get_object_or_404(Product, id=product_id)
        job.delete()
        messages.success(request, 'Product Deleted Successfully.')
        return redirect('productsUrl')

def profile_views(request):
    return render(request, 'admin/profile.html')

def upload_product(request):
    if request.method == 'POST':
        form = ProductRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            barcode_image = form.cleaned_data.get(
                'barcode_image')  # Safely get the image
            
            # Save the product data to the database
            product = Product.objects.create(
                admin=request.user,  # Assuming the logged-in user is the admin
                product_name=form.cleaned_data['product_name'],
                product_code=form.cleaned_data['product_code'],
                price=form.cleaned_data['price'],
                quantity=form.cleaned_data['quantity'],
                expiry_date=form.cleaned_data['expiry_date']
            )
            product.save()

            # Add success message
            messages.success(
                request, 'Product registered successfully!')

            # Redirect to products page (change 'products_page_url' to your URL name)
            return redirect('productsUrl')
        else:
            print(form.errors)  # Debugging form errors

    else:
        form = ProductRegistrationForm()

    return render(request, 'admin/scan_product.html', {'form': form})

