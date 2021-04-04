from django.urls import path

from . import views

urlpatterns = [
    path('clients/', views.client_list)
]
