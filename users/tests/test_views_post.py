import re

from django.urls import reverse
import pytest

# TODO: Implement special method for password-reset-confirm


class TestUsersPostMethod:

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, data, expected_response, num_expected",
        [
            ('users:login', {}, {},
             'This field is required', 2),
            ('users:register', {}, {},
             'This field is required', 6),
            ('users:password-reset', {}, {},
             'This field is required', 1),
        ]
    )
    def test_users_empty_data(
        self,
        view_namespace_url,
        kwargs,
        data,
        expected_response,
        num_expected,
        client
    ):
        """ Test clients are unregistered here but should be able to post
        data in these views. The data is empty here and there should be
        <num_expected> instances of <expected_response> in the response
        content """

        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.post(url, data=data)
        response_content = response.content.decode()

        assert response.status_code == 200
        assert len(list(re.finditer(expected_response,
                                    response_content))) is num_expected

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, data, expected_response, num_expected",
        [
            ('users:profile-update',
             {'username': 'testuser'}, {},
             'This field is required', 8),
            ('users:password-change', {}, {},
             'This field is required', 3),
        ]
    )
    def test_users_empty_data_registered(
        self,
        view_namespace_url,
        kwargs,
        data,
        expected_response,
        num_expected,
        login_user
    ):
        """ Test clients are registered here and should be able to post data in 
        these views. The data is empty here and there should be <num_expected> 
        instances of <expected_response> in the response content """

        user, client = login_user()
        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.post(url, data=data)
        response_content = response.content.decode()

        assert response.status_code == 200
        assert len(list(re.finditer(expected_response,
                                    response_content))) is num_expected

# TODO: Fix all tests underneath

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, data, expected_response, num_expected",
        [
            ('users:login', {}, {'username': 'testuser'},

             'This field is required', 1),
            ('users:login', {}, {'password': 'testpassword'},

             'This field is required', 1),

            ('users:register', {}, {'username': 'testuser'},

             'This field is required', 5),
            ('users:register', {}, {'first_name': 'testfn'},

             'This field is required', 5),
            ('users:register', {}, {'last_name': 'testln'},

             'This field is required', 5),
            ('users:register', {}, {'email': 'test@email.com'},

             'This field is required', 5),
            ('users:register', {}, {'password1': 'testpassword'},

             'This field is required', 5),
            ('users:register', {}, {'password2': 'testpassword'},

             'This field is required', 5),
            ('users:register', {}, {
                'username': 'testuser',
                'first_name': 'testfn'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'username': 'testuser',
                'last_name': 'testln'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'username': 'testuser',
                'email': 'test@email.com'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'username': 'testuser',
                'password1': 'testpassword'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'username': 'testuser',
                'password2': 'testpassword'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'first_name': 'testfn',
                'last_name': 'testln'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'first_name': 'testfn',
                'email': 'test@email.com'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'first_name': 'testfn',
                'password1': 'testpassword'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'first_name': 'testfn',
                'password2': 'testpassword'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'last_name': 'testln',
                'email': 'test@email.com'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'last_name': 'testln',
                'password1': 'testpassword'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'last_name': 'testln',
                'password2': 'testpassword'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'email': 'test@email.com',
                'password1': 'testpassword'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'email': 'test@email.com',
                'password2': 'testpassword'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'password1': 'testpassword',
                'password2': 'testpassword'
            },
                'This field is required', 4),
            ('users:register', {}, {
                'username': 'testuser', 'first_name': 'testfn',
                'last_name': 'testln'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'username': 'testuser', 'first_name': 'testfn',
                'email': 'test@email.com'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'username': 'testuser', 'first_name': 'testfn',
                'password1': 'testpassword'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'username': 'testuser', 'first_name': 'testfn',
                'password2': 'testpassword'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'username': 'testuser', 'last_name': 'testln',
                'email': 'test@email.com'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'username': 'testuser', 'last_name': 'testln',
                'password1': 'testpassword'},
             'This field is required', 3),
            ('users:register', {}, {
                'username': 'testuser', 'last_name': 'testln',
                'password2': 'testpassword'},
             'This field is required', 3),
            ('users:register', {}, {
                'username': 'testuser', 'email': 'test@email.com',
                'password1': 'testpassword'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'username': 'testuser', 'email': 'test@email.com',
                'password2': 'testpassword'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'username': 'testuser', 'password1': 'testpassword',
                'password2': 'testpassword'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'first_name': 'testfn', 'last_name': 'testln',
                'email': 'test@email.com'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'first_name': 'testfn', 'last_name': 'testln',
                'password1': 'testpassword'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'first_name': 'testfn', 'last_name': 'testln',
                'password2': 'testpassword'},
             'This field is required', 3),
            ('users:register', {}, {
                'first_name': 'testfn', 'email': 'test@email.com',
                'password1': 'testpassword'},
             'This field is required', 3),
            ('users:register', {}, {
                'first_name': 'testfn', 'email': 'test@email.com',
                'password2': 'testpassword'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'last_name': 'testln', 'email': 'test@email.com',
                'password1': 'testpassword'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'last_name': 'testln', 'email': 'test@email.com',
                'password2': 'testpassword'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'email': 'test@email.com', 'password1': 'testpassword',
                'password2': 'testpassword'
            },
                'This field is required', 3),
            ('users:register', {}, {
                'username': 'testuser', 'first_name': 'testfn',
                'last_name': 'testln', 'email': 'test@email.com'
            },
                'This field is required', 2),
            ('users:register', {}, {
                'username': 'testuser', 'first_name': 'testfn',
                'last_name': 'testln', 'password1': 'testpassword'
            },
                'This field is required', 2),
            ('users:register', {}, {
                'username': 'testuser', 'first_name': 'testfn',
                'last_name': 'testln', 'password2': 'testpassword'
            },
                'This field is required', 2),
            ('users:register', {}, {
                'first_name': 'testfn', 'last_name': 'testln',
                'email': 'test@email.com', 'password1': 'testpassword'
            },
                'This field is required', 2),
            ('users:register', {}, {
                'first_name': 'testfn', 'last_name': 'testln',
                'email': 'test@email.com', 'password2': 'testpassword'
            },
                'This field is required', 2),
            ('users:register', {}, {
                'username': 'testuser', 'email': 'test@email.com',
                'password1': 'testpassword', 'password2': 'testpassword'
            },
                'This field is required', 2),
            ('users:register', {}, {
                'last_name': 'testln', 'email': 'test@email.com',
                'password1': 'testpassword', 'password2': 'testpassword'
            },
                'This field is required', 2),
            ('users:register', {}, {
                'username': 'testuser', 'last_name': 'testln',
                'password1': 'testpassword', 'password2': 'testpassword'
            },
                'This field is required', 2),
            ('users:register', {}, {
                'username': 'testuser', 'first_name': 'testfn',
                'email': 'test@email.com', 'password2': 'testpassword'
            },
                'This field is required', 2),
            ('users:register', {}, {
                'username': 'testuser',
                'first_name': 'testfn', 'last_name': 'testln',
                'email': 'test@email.com', 'password1': 'testpassword'

            },
                'This field is required', 1),
            ('users:register', {}, {
                'username': 'testuser',
                'first_name': 'testfn', 'last_name': 'testln',
                'email': 'test@email.com',
                'password2': 'testpassword'
            },
                'This field is required', 1),
            ('users:register', {}, {
                'username': 'testuser',
                'first_name': 'testfn', 'last_name': 'testln',
                'password1': 'testpassword',
                'password2': 'testpassword'
            },
                'This field is required', 1),
            ('users:register', {}, {
                'username': 'testuser', 'first_name': 'testfn',
                'email': 'test@email.com',
                'password1': 'testpassword',
                'password2': 'testpassword'
            },
                'This field is required', 1),
            ('users:register', {}, {
                'username': 'testuser',
                'last_name': 'testln', 'email': 'test@email.com',
                'password1': 'testpassword', 'password2': 'testpassword'
            },
                'This field is required', 1),
            ('users:register', {}, {
                'first_name': 'testfn',
                'last_name': 'testln', 'email': 'test@email.com',
                'password1': 'testpassword',
                'password2': 'testpassword'
            },
                'This field is required', 1),
        ]
    )
    def test_users_partial_data(
        self,
        view_namespace_url,
        kwargs,
        data,
        expected_response,
        num_expected,
        client,
    ):
        """ Test clients are unregistered here but should be able to 
        post data in these views. The data is partially complete here and 
        there should be <num_expected> instances of <expected_response> 
        in the response content """

        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.post(url, data=data)
        response_content = response.content.decode()

        assert response.status_code == 200
        assert len(list(re.finditer(expected_response,
                                    response_content))) is num_expected

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, data, expected_response, num_expected",
        [
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn'},
             'This field is required', 7),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln'},
             'This field is required', 7),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com'},
             'This field is required', 7),
            ('users:profile-update', {'username': 'testuser'},
             {'user_bio': 'test-bio'},
             'This field is required', 7),
            ('users:profile-update', {'username': 'testuser'},
             {'country': 'India'},
             'This field is required', 7),
            ('users:profile-update', {'username': 'testuser'},
             {'gender': 'male'},
             'This field is required', 7),
            ('users:profile-update', {'username': 'testuser'},
             {'birth_date': '11/11/2001'},
             'This field is required', 7),
            ('users:profile-update', {'username': 'testuser'},
             {'visible': 'off'},
             'This field is required', 7),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'last_name': 'testln'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'email': 'test@email.com'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'user_bio': 'test-bio'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'country': 'India'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'gender': 'male'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'birth_date': '11/11/2001'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'visible': 'off'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'email': 'test@email.com'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'user_bio': 'test-bio'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'country': 'India'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'gender': 'male'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'birth_date': '11/11/2001'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'visible': 'off'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'user_bio': 'test-bio'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'country': 'India'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'gender': 'male'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'birth_date': '11/11/2001'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'visible': 'off'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'user_bio': 'test-bio', 'country': 'India'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'user_bio': 'test-bio', 'gender': 'male'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'user_bio': 'test-bio', 'birth_date': '11/11/2001'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'user_bio': 'test-bio', 'visible': 'off'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'country': 'India', 'gender': 'male'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'country': 'India', 'birth_date': '11/11/2001'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'country': 'India', 'visible': 'off'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'gender': 'male', 'birth_date': '11/11/2001'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'gender': 'male', 'visible': 'off'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'birth_date': '11/11/2001', 'visible': 'off'},
             'This field is required', 6),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'last_name': 'testln',
             'email': 'test@email.com' },
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'last_name': 'testln', 
             'user_bio': 'test-bio'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'last_name': 'testln', 
             'country': 'India'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'last_name': 'testln', 
             'gender': 'male'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'last_name': 'testln', 
             'birth_date': '11/11/2001'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'last_name': 'testln', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'email': 'test@email.com', 
             'user_bio': 'test-bio'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'email': 'test@email.com', 
             'country': 'India'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'email': 'test@email.com', 
             'gender': 'male'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'email': 'test@email.com', 
             'birth_date': '11/11/2001'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'email': 'test@email.com', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'user_bio': 'test-bio', 
             'country': 'India'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'user_bio': 'test-bio', 
             'birth_date': '11/11/2001'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'user_bio': 'test-bio', 
             'visible': 'off'},
             'This field is required', 5), 
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'country': 'India', 
             'gender': 'male'} ,
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'country': 'India', 
             'birth_date': '11/11/2001'},
             'This field is required', 5), 
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'country': 'India', 
             'visible': 'off'},
             'This field is required', 5), 
            ('users:profile-update', {'username': 'testuser'},
             {'first_name': 'testfn', 'birth_date': '11/11/2001', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'email': 'test@email.com', 
             'user_bio': 'test-bio'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'email': 'test@email.com', 
             'country': 'India'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'email': 'test@email.com', 
             'gender': 'male'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'email': 'test@email.com', 
             'birth_date': '11/11/2001'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'email': 'test@email.com', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'user_bio': 'test-bio', 
             'country': 'India'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'user_bio': 'test-bio', 
             'gender': 'male'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'user_bio': 'test-bio', 
             'birth_date': '11/11/2001'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'user_bio': 'test-bio', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'country': 'India', 
             'gender': 'male'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'country': 'India', 
             'birth_date': '11/11/2001'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'country': 'India', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'gender': 'male', 
             'birth_date': '11/11/2001'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'gender': 'male', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'last_name': 'testln', 'birth_date': '11/11/2001', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'user_bio': 'test-bio', 
             'country': 'India'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'user_bio': 'test-bio', 
             'gender': 'male'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'user_bio': 'test-bio', 
             'birth_date': '11/11/2001'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'user_bio': 'test-bio', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'country': 'India', 
             'gender': 'male'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'country': 'India', 
             'birth_date': '11/11/2001'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'country': 'India', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'gender': 'male', 
             'birth_date': '11/11/2001'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'gender': 'male', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'email': 'test@email.com', 'birth_date': '11/11/2001', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'user_bio': 'test-bio', 'country': 'India', 
             'gender': 'male'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'user_bio': 'test-bio', 'country': 'India', 
             'birth_date': '11/11/2001'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'user_bio': 'test-bio', 'country': 'India', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'user_bio': 'test-bio', 'gender': 'male', 
             'birth_date': '11/11/2001'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'user_bio': 'test-bio', 'gender': 'male', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'user_bio': 'test-bio', 'birth_date': '11/11/2001', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'country': 'India', 'gender': 'male', 
             'birth_date': '11/11/2001'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'country': 'India', 'gender': 'male', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:profile-update', {'username': 'testuser'},
             {'gender': 'male', 'birth_date': '11/11/2001', 
             'visible': 'off'},
             'This field is required', 5),
            ('users:password-change', {}, {'old_password':'test-pass'},
             'This field is required', 2),
            ('users:password-change', {}, {'new_password1':'new-pass'},
             'This field is required', 2),
            ('users:password-change', {}, {'new_password2':'new-pass'},
             'This field is required', 2),
            ('users:password-change', {}, {'old_password':'test-pass', 'new_password1':'new-pass'},
             'This field is required', 1),
            ('users:password-change', {}, {'old_password':'test-pass', 'new_password2':'new-pass'},
             'This field is required', 1),
            ('users:password-change', {}, {'new_password1':'new-pass', 'new_password2':'new-pass'},
             'This field is required', 1),
             
        ]
    )
    def test_users_partial_data_registered(
        self,
        view_namespace_url,
        kwargs,
        data,
        expected_response,
        num_expected,
        login_user
    ):
        """ Test clients are registered here and they should be able to 
        post data in these views. The data is partially complete here and 
        there should be <num_expected> instances of <expected_response> in the 
        response content """

        user, client = login_user()
        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.post(url, data=data)
        response_content = response.content.decode()

        assert response.status_code == 200
        assert len(list(re.finditer(expected_response,
                                    response_content))) is num_expected

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, data, expected_response, num_expected",
        [
            ('home:contact', {}, {
                'from_email': 'testemail.com', 'message': 'test message body',
                'subject': 'test subject'
            },
                'Enter a valid email', 1),
            ('home:contact', {}, {
                'from_email': 'test@email.com',
                'message': '', 'subject': ''
            },

                'This field is required', 2),
        ]
    )
    def test_users_invalid_data(
        self,
        view_namespace_url,
        kwargs,
        data,
        expected_response,
        num_expected,
        client
    ):
        """ Test clients are unregistered here but should be able to
        post data in these views. The data is complete here, but 
        invalid and there should be <num_expected> instances of
        <expected_response> in the response content """

        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.post(url, data=data)
        response_content = response.content.decode()

        assert response.status_code == 200
        assert len(list(re.finditer(expected_response,
                                    response_content))) is num_expected


@pytest.mark.unittest
class TestInteractionsPostMethodValid:
    """ The data submitted here should be completely valid. Tests 
    should not be parameterized here, unless they really need to be. """

    def test_home_contact_email(
        self,
        client
    ):
        """ Test clients are unregistered here but should be able to post 
        data in these views. The data is complete and valid here and the 
        data sent through form should be present in the mail inbox """

        # url = reverse('home:contact')

        # data = {'from_email': 'test@email.com',
        #         'message':
        #         'This is a test message', 'subject':
        #         'This is a test subject'}

        # response = client.post(url, data=data, follow=True)

        # assert response.status_code == 200
        # assert len(mail.outbox) == 1, "Inbox is not empty"
        # assert mail.outbox[0].subject == data['subject']
        # assert mail.outbox[0].body == data['message']
        # assert mail.outbox[0].from_email == data['from_email']
        # assert mail.outbox[0].to == [settings.EMAIL_HOST_USER] if settings.EMAIL_HOST_USER else [
        #     'ocean-pv_dev@email.com']
