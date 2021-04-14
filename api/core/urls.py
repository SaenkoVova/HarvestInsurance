from django.urls import path
from . import views

urlpatterns = [
    path('police/', views.PolicesListView.as_view()),
    path('docs/', views.DocListView.as_view()),
    path('create_doc/', views.DocCreateView.as_view()),
    path('create_ukraine_passport/', views.UkrainePassportCreateView.as_view()),
    path('register/', views.ClientCreateView.as_view()),
]
