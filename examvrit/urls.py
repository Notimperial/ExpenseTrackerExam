
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # API authentication endpoints (from home/auth_urls.py)
    path('api/auth/', include('home.auth_urls')), #  handle /api/auth/register/, /api/auth/login/, /api/auth/refresh/

    # API expense/income endpoints (from home/urls.py)
    path('api/', include('home.urls')), #  handle /api/expenses/
]