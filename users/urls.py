from django.urls import path
from django.contrib.auth import views as auth_views

from users.views import (
    register,
    ProfileView,
    UserLoginView,
    update_profile_view,
    result_view,
    password_change_view,
    UserPasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'users'

urlpatterns = [
    path('results/<str:username>/', result_view, name='results'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/<str:username>/', ProfileView.as_view(), name='profile'),
    path('profile/<str:username>/update/',
         update_profile_view, name='profile-update'),

    path('password-change/', password_change_view, name='password-change'),
    path('password-change/done/', UserPasswordChangeDoneView.as_view(),
         name='password-change-done'),

    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(),
         name='password-reset-done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password-reset-confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(),
         name='password-reset-complete'),
]
