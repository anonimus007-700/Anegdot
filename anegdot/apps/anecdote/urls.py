from . import views
from django.urls import path

app_name = 'anecdote'
urlpatterns = [
    path('', views.index, name="reading")
]
