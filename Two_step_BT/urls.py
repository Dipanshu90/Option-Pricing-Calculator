from django.urls import path
from . import views

app_name = 'two_step'

urlpatterns = [
    path('', views.home, name='two_step'),
    path('two_step_result', views.two_step_calc, name='calc_2_step'),
]
