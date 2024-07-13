from django.urls import path
from .views import *

urlpatterns = [
    path('branches/', BranchAPIView.as_view()),
    path('branches/<int:pk>/', BranchDetailAPIView.as_view()),
    path('banks/', BanksAPIView.as_view()),
    path('banks/<int:pk>/', BankDetailAPIView.as_view()),
    path('create-accounts/', CreateAccountAPIView.as_view()),
    path('accounts/', AccountsAPIView.as_view()),
    path('accounts/<int:pk>/', AccountDetailAPIView.as_view()),
    path('deposits/', DepositAPIView.as_view()),
    path('withdraws/', WithdrawAPIView.as_view()),
    
]