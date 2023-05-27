from django.urls import path
from . import views

app_name = 'n_step'

urlpatterns = [
    path('', views.home_n, name='n_step'),
    path('n_step_result', views.n_step_calc, name='calc_n_step'),
]
