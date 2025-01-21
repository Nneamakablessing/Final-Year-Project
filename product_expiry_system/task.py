# task.py in your Django app
from django.utils import timezone
from django.core.mail import send_mail
from .models import Product
import logging
from datetime import timedelta

logger = logging.getLogger(__name__)

def check_expired_products():
    today = timezone.now().date()
    expired_products = Product.objects.filter(expiry_date__lt=today)

    if expired_products.exists():
        for product in expired_products:
            admin_email = product.admin.email
            subject = f"Product Expiry Alert: {product.product_name}"
            message = f"The product '{product.product_name}' (Code: {product.product_code}) has expired on {product.expiry_date}."
            print(message)
            print(admin_email)  

            # Send email to the admin
            send_mail(
                subject,
                message,
                'noreply@yourdomain.com',
                [admin_email],
                fail_silently=False,
            )
            logger.info(f'Email sent for expired product: {product.product_name}')
    else:
        logger.info('No expired products found')


# New function to notify admin 14 days before the product expiry date
def notify_products_expiring_soon():
    today = timezone.now().date()
    soon_to_expire_date = today + timedelta(days=14)  # Check products expiring in 14 days

    # Query products that will expire in 14 days
    soon_to_expire_products = Product.objects.filter(expiry_date=soon_to_expire_date)

    if soon_to_expire_products.exists():
        for product in soon_to_expire_products:
            admin_email = product.admin.email
            subject = f"Upcoming Product Expiry Alert: {product.product_name}"
            message = f"The product '{product.product_name}' (Code: {product.product_code}) will expire on {product.expiry_date}. Please take necessary actions."

            print(message) 
            print(admin_email) 

            # Send email to the admin
            send_mail(
                subject,
                message,
                'noreply@yourdomain.com', 
                [admin_email],
                fail_silently=False,
            )
            logger.info(f'Notification sent for product expiring soon: {product.product_name}')
    else:
        logger.info('No products expiring in 14 days')
