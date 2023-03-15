from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path('transaction/', views.TransactionView.as_view(), name="transaction"),
    path('users/', views.UserListView.as_view(), name="users")
]
