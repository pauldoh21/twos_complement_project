from django.urls import path 
from TwosComplement import views

app_name = 'TwosComplement'

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about, name='about_us'),
    path('login/', views.login, name='login'),
    path('login/my_dates/', views.myDates, name='my_dates'),
    path('register/', views.register, name='register'),
    path('register/compatibility_questionnaire/', views.questionnaire, name='compatibility'),
    path('login/my_dates/my_account/', views.myAccount, name='my_account'),
    path('login/my_dates/manage/', views.manage, name='manage'),
]