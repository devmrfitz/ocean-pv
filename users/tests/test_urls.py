from django.test import SimpleTestCase
import pytest
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User

from users.views import (
    register,
    ProfileView,
    UserLoginView,
    result_view,
    update_profile_view,
    password_change_view,
    UserPasswordChangeDoneView
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
