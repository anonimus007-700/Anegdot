from . import views
from django.urls import path

app_name = 'poll'
urlpatterns = [
    path('', views.index, name="poll"),
    path('offers/', views.offers, name="offers")
]
