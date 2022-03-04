from django.urls import path 
from TwosComplement import views

app_name = 'TwosComplement'

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about, name='about_us'),
    path('login/', views.login, name='login'),
]