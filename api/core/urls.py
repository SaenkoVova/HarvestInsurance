from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateAPIView, DocumentCreateView, DocumentsLoadView, \
    DocumentDestroyView, CalculatePriceView, OrdersLoadView, CreatePoliceView,\
    OrderDetailsLoadView, NotificationsLoadView, NotificationsReadView, NotificationsDeleteView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('user', UserRetrieveUpdateAPIView.as_view()),
    path('uploadDocument/', DocumentCreateView.as_view()),
    path('loadUserDocuments/', DocumentsLoadView.as_view()),
    path('deleteDocument/', DocumentDestroyView.as_view()),
    path('getPrice/', CalculatePriceView.as_view()),
    path('loadUserOrders/', OrdersLoadView.as_view()),
    path('createPolice/', CreatePoliceView.as_view()),
    path('loadOrderDetails/', OrderDetailsLoadView.as_view()),
    path('loadNotifications/', NotificationsLoadView.as_view()),
    path('readNotifications/', NotificationsReadView.as_view()),
    path('deleteNotification/', NotificationsDeleteView.as_view())
]
