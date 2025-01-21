from django.urls import path, include
from product_expiry_system import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('account/dashboard/', views.dashboard_views, name="dashboardUrl"),
    path('account/products/', views.products_views, name="productsUrl"),
    path('account/profile/', views.profile_views, name="profileUrl"),
    path('account/delete-product/', views.delete_product, name="deleteProductUrl"),
    # path('scan/', views.scan_qr_code, name='scan_qr_code'),
    path('account/scan-product/', views.upload_product, name="scanProductUrl"),
    path("auth/", include("django.contrib.auth.urls")),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]

