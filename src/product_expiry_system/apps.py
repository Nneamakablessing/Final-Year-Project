from django.apps import AppConfig
import threading
import time
from django.utils import timezone

class ProductExpirySystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product_expiry_system'

    def ready(self):
        # Ensure this code is executed only once in the app lifecycle
        if not any([thread.name == 'ExpiryCheckThread' for thread in threading.enumerate()]):
            # Start the background thread
            thread = threading.Thread(target=start_expiry_check)
            # Give the thread a unique name
            thread.setName('ExpiryCheckThread')
            thread.daemon = True  # Daemonize thread to shut down with the server
            thread.start()

def start_expiry_check():
    """
    This function starts the infinite loop that checks for both expired products
    and products expiring in 14 days. It runs continuously every hour.
    """
    time.sleep(5)  # Optional sleep to allow Django to fully load apps
    while True:
        from .task import check_expired_products, notify_products_expiring_soon

        # Check for expired products
        check_expired_products()

        # Notify about products expiring in 14 days
        notify_products_expiring_soon()

        # Run both checks every hour (3600 seconds)
        time.sleep(3600)
