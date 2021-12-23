from django.contrib import admin
from django.urls import path
from accounts.views import signup,signin,signout

urlpatterns = [
    path('signup',signup ,name='signup'),
    path('signin',signin,name='signin'),
    path('signout',signout ,name='signout'),
]
