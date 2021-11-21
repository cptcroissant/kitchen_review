from django.urls import path

from . import views


app_name = 'herokunlp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('home_2/', views.ResView.as_view(), name='home_2')
]
