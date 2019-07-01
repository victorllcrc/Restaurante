"""restaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from rest_framework.authtoken import views

urlpatterns = [

    # path se contact
    path('deadpool/', include('deadpool.urls')),


# path se reserva
    path('reserva/', include('reserva.urls')),

    # path se contact
    path('contact/', include('contact.urls')),

    # path se blog
    path('blog/', include('blog.urls')),

    # path se pages
    path('page/', include('pages.urls')),

    #paths del core
    path('', include('core.urls')),

    #path se services
    path('services/', include('services.urls')),

    #paths del admin
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('deadpoll/auth', include('rest_framework.urls')),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#Personalizar los titulos del admin
admin.site.site_header = "El Puntillo Criollo"
admin.site.index_title = "PANEL DE ADMINISTRACIÓN"
admin.site.site_title = "El Puntillo Criollo"
