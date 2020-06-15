from django.test import SimpleTestCase
import pytest
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

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


@pytest.mark.parametrize(
    "reverse_url, kwargs, resolve_url, view_func, class_based",
    [
        ('users:register', {}, '/users/register/', register, False),
        ('users:results', {'username': 'testuser'},
         '/users/results/testuser/', result_view, False),
        ('users:profile-update',
         {'username': 'testuser'}, '/users/profile/testuser/update/', update_profile_view, False),
        ('users:password-change', {}, '/users/password-change/',
         password_change_view, False),
        ('users:profile', {'username': 'testuser'},
         '/users/profile/testinguser/', ProfileView, True),
        ('users:login', {}, '/users/login/', UserLoginView, True),
        ('users:logout', {}, '/users/logout/', auth_views.LogoutView, True),
        ('users:password-change-done', {}, '/users/password-change/done/',
         UserPasswordChangeDoneView, True),
         ('users:password-reset', {}, '/users/password-reset/',
         PasswordResetView, True),
         ('users:password-reset-done', {}, '/users/password-reset/done/',
         PasswordResetDoneView, True),
         ('users:password-reset-confirm', {'uidb64':'27c80dab7a26c5e1', 'token':'27c80dab7a26c5e1'}, '/users/password-reset/confirm/27c80dab7a26c5e1/27c80dab7a26c5e1/',
         PasswordResetConfirmView, True),
         ('users:password-reset-complete', {}, '/users/password-reset/complete/',
         PasswordResetCompleteView, True),
    ]
)
def test_users_urls(
    return_views,
    reverse_url,
    kwargs,
    resolve_url,
    view_func,
    class_based
):
    """ Test app-> users urls """

    reverse_view, resolve_view = return_views(reverse_url, resolve_url, kwargs)

    if not class_based:
        assert reverse_view.func == view_func
        assert resolve_view.func == view_func
    else:
        assert reverse_view.func.view_class == view_func
        assert resolve_view.func.view_class == view_func
