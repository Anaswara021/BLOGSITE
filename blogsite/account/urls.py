from django.urls import path
from .views import *

urlpatterns = [
    path('regi/',Signup.as_view(),name="regi"),
    path('logi/',Signin.as_view(),name="logi"),
    path('logo/',SignOut.as_view(),name="logo")
]