"""ogunkuade_pdf_tools URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from pdf_tools import views as pdf_tools_views





urlpatterns = [
    path('admin/', admin.site.urls),

    path('', pdf_tools_views.home, name='home'),

    path('merge_pdf/', pdf_tools_views.merge_pdf, name='merge_pdf'),
    path('merge_pdf_complete/', pdf_tools_views.merge_pdf_complete, name='merge_pdf_complete'),

    path('password_pdf/', pdf_tools_views.password_pdf, name='password_pdf'),
    path('password_pdf_complete/', pdf_tools_views.password_pdf_complete, name='password_pdf_complete'),

]





if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

