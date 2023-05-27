from django.urls import path
from . import views

app_name = 'black_scholes'

urlpatterns = [
    path('', views.home, name='bs'),
    path('bs_result', views.black_scholes, name='bs-result'),
]
