from django.urls import path, include
from . import views
urlpatterns = [
    path('bankAdmin', views.bank_admin, name="bank_admin"),
    #path('', include('users.urls')),
    #path('bank/', include('bank.urls')),
]