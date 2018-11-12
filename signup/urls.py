from django.urls import path
from django.contrib.auth import views as authViews

from . import views

urlpatterns = [
    path('sign/', views.SignupView.as_view(), name="signup"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', authViews.LogoutView.as_view(), name='logout'),

    path('password_change/', authViews.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', authViews.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('password_reset/', authViews.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]