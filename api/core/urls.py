from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView, DocumentCreateView, DocumentsLoadView, DocumentDestroyView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('user', UserRetrieveUpdateAPIView.as_view()),
    path('uploadDocument/', DocumentCreateView.as_view()),
    path('loadUserDocuments/', DocumentsLoadView.as_view()),
    path('deleteDocument/', DocumentDestroyView.as_view())
]
