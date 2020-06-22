import re

from django.urls import reverse
import pytest


class TestUsersViewsGetMethod:

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, template_name",
        [
            ('users:profile', {'username': 'testinguser'},
             'users/profile.html'),
            ('users:results', {'username': 'testinguser'},
             'users/results.html'),
            ('users:profile-update',
             {'username': 'testinguser'}, 'users/user profile_form.html'),

            ('users:password-change', {}, 'users/password_change_form.html'),
            ('users:password-change-done', {},
             'users/password_change_done.html'),
            ('users:answer-profiles', {'pk': 1},
             '/users/selfanswergroup_list.html'),
        ]
    )
    def test_users_views_unregistered(
        self,
        view_namespace_url,
        kwargs,
        template_name,
        client
    ):
        """ Test clients are unregistered here and shouldn't be able to 
        access these views """

        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.get(url)

        assert response.status_code == 302
        assert template_name not in [t.name for t in response.templates]

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, template_name",
        [
            ('users:login', {}, 'users/login.html'),
            ('users:logout', {}, 'users/logout.html'),
            ('users:register', {}, 'users/register.html'),

            ('users:password-reset', {},
             'users/password_reset/password_reset_form.html'),
            ('users:password-reset-done', {},
             'users/password_reset/password_reset_done.html'),
            ('users:password-reset-confirm',
             {'token': 'uMMOt9DTk3L9ETVt7gDjkJXzZ3P7KKAKdYViuyJQmWE',
              'uidb64': 'X2k'},
             'users/password_reset/password_reset_confirm.html'),
            ('users:password-reset-complete', {},
             'users/password_reset/password_reset_complete.html'),
        ]
    )
    def test_users_views(
        self,
        view_namespace_url,
        kwargs,
        template_name,
        client
    ):
        """ Test clients are unregistered here but should be able to access 
        these views """

        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.get(url)

        assert response.status_code == 200
        assert template_name in [t.name for t in response.templates]

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, template_name",
        [
            ('users:profile', {'username': 'testinguser'},
             'users/profile.html'),
            ('users:results', {'username': 'testinguser'},
             'users/results.html'),
            ('users:profile-update',
             {'username': 'testinguser'}, 'users/userprofile_form.html'),
            ('users:password-change', {}, 'users/password_change_form.html'),
            ('users:password-change-done', {},
             'users/password_change_done.html'),
            ('users:answer-profiles', {'pk': 1},
             'interactions/selfanswergroup_list.html')

        ]
    )
    def test_users_views_registered(
        self,
        view_namespace_url,
        kwargs,
        template_name,
        login_user,
    ):
        """ Test clients are registered here and they should be able to 
        access these views """

        user, client = login_user()
        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.get(url)

        assert response.status_code == 200
        assert template_name in [t.name for t in response.templates]


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
             {'country': 'Enter'},
             'This field is required', 7),
            ('users:profile-update', {'username': 'testuser'},
             {'gender': 'male'},
             'This field is required', 7),
            ('users:profile-update', {'username': 'testuser'},
             {'birth_date': '11/11/2001'},
             'This field is required', 7),
            ('users:profile-update', {'username': 'testuser'},
             {'visible': 'False'},
             'This field is required', 7),

            ('users:password-change', {}, {},
             'This field is required', 3),
        ]
    )
    @pytest.mark.testing
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
                'from_email': 'test@email.com', 'message': '',
                'subject': ''
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


class TestInteractionsPostMethodValid:
    """ The data submitted here should be completely valid. Tests 
    should not be parameterized here, unless they really need to be. """

    @pytest.mark.testing
    def test_home_contact_email(
        self,
        client
    ):
        """ Test clients are unregistered here but should be able to post 
        data in these views. The data is complete and valid here and the 
        data sent through form should be present in the mail inbox """

        url = reverse('home:contact')

        data = {'from_email': 'test@email.com',
                'message':
                'This is a test message', 'subject':
                'This is a test subject'}

        response = client.post(url, data=data, follow=True)

        # assert response.status_code == 200
        # assert len(mail.outbox) == 1, "Inbox is not empty"
        # assert mail.outbox[0].subject == data['subject']
        # assert mail.outbox[0].body == data['message']
        # assert mail.outbox[0].from_email == data['from_email']
        # assert mail.outbox[0].to == [settings.EMAIL_HOST_USER] if settings.EMAIL_HOST_USER else [
        #     'ocean-pv_dev@email.com']
