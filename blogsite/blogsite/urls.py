"""blogsite URL Configuration

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
from django.urls import path,include
# from django.conf import settings
# from django.conf.urls.static import static
from account.views import Homee
from user.views import User
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accnt/',include("account.urls")),
    path('uh/',include("user.urls")),
    path('home/',Homee.as_view(),name='home'),
    # path('uh/',User.as_view(),name='uh')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
