"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Shop'
admin.site.index_title = 'Shop'

urlpatterns = [
    path('', include('page.urls')),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('cart/', include('cart.urls')),
    path('store/', include('store.urls')),
    path('payment/', include('payment.urls')),
    path('account/', include('account.urls')),
    path('account/', include('django.contrib.auth.urls')),
    
    path('unicorn/', include('django_unicorn.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]
