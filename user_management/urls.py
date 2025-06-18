from .views import LoginAPIView, RegisterAPIView, CustomersAPIView
from django.urls import path

urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('customers', CustomersAPIView.as_view()),
]
