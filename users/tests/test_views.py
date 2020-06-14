from django.urls import resolve, reverse
import pytest


class TestInteractionsViewsGetMethod:

    @pytest.mark.parametrize(
        "view_namespace_url, args, template_name",
        [
            ('users:profile', ['testinguser'], 'users/profile.html'),
            ('users:profile-update',
             ['testuser'], 'users/user profile_form.html')
        ]
    )
    def test_users_views_unregistered(
            self,
        view_namespace_url,
        args,
        template_name,
        client
    ):
        """ Test clients are unregistered here and shouldn't be able to access these views """
        url = reverse(view_namespace_url, args=args if args else None)
        response = client.get(url)

        assert response.status_code == 302
        assert template_name not in [t.name for t in response.templates]

    @pytest.mark.parametrize(
        "view_namespace_url, args, template_name",
        [
            ('users:login', [], 'users/login.html'),
            ('users:logout', [], 'users/logout.html'),
            ('users:register', [], 'users/register.html'),
        ]
    )
    def test_users_views(
            self,
        view_namespace_url,
        args,
        template_name,
        client
    ):
        """ Test clients are unregistered here but should be able to access these views """

        url = reverse(view_namespace_url, args=args if args else None)
        response = client.get(url)

        assert response.status_code == 200
        assert template_name in [t.name for t in response.templates]

    @pytest.mark.parametrize(
        "view_namespace_url, args, template_name",
        [
            ('users:profile', ['testinguser'], 'users/profile.html'),
            ('users:profile-update',
             ['testuser'], 'users/userprofile_form.html')
        ]
    )
    def test_users_views_registered(
        self,
            view_namespace_url,
            args,
            template_name,
            login_user,
    ):
        """ Test clients are registered here and they should be able to access these views """

        user, client = login_user()
        url = reverse(view_namespace_url, args=args if args else None)
        response = client.get(url)

        assert response.status_code == 200
        assert template_name in [t.name for t in response.templates]
