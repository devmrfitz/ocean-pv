import re

from django.urls import resolve, reverse
import pytest


class TestHomeGetMethod:

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, template_name",
        [
            ('home:home', {}, 'home/home.html'),
            ('home:contact-done', {}, 'home/contact_done.html'),
            ('home:contact', {}, 'home/contact.html'),
            ('home:resources', {}, 'home/resources.html')
        ]
    )
    def test_home_views(
        self,
        view_namespace_url,
        kwargs,
        template_name,
        client
    ):
        """ Test clients are unregistered here but should be able to access these views """

        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.get(url)

        assert response.status_code == 200
        assert template_name in [t.name for t in response.templates]


class TestHomePostMethod:

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, data, expected_response, num_expected",
        [
            ('home:contact', {}, {}, 'This field is required', 3),
        ]
    )
    def test_home_empty_data(
        self,
        view_namespace_url,
        kwargs,
        data,
        expected_response,
        num_expected,
        client
    ):
        """ Test clients are unregistered here but should be able to post data in these views. The data is empty here and there should be <num_expected> instances of <expected_response> in the response content """

        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.post(url, data=data)
        response_content = response.content.decode()

        assert response.status_code == 200
        assert len(list(re.finditer(expected_response,
                                    response_content))) is num_expected

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, data, expected_response, num_expected",
        [
            ('home:contact', {}, {'from_email': 'testemail@email.com'},
             'This field is required', 2),
            ('home:contact', {}, {'subject': 'test subject'},
             'This field is required', 2),
            ('home:contact', {}, {'message': 'test message body'},
             'This field is required', 2),
            ('home:contact', {}, {'from_email': 'testemail@email.com',
                                  'message': 'test message body'}, 'This field is required', 1),
        ]
    )
    def test_home_partial_data(
        self,
        view_namespace_url,
        kwargs,
        data,
        expected_response,
        num_expected,
        client
    ):
        """ Test clients are unregistered here but should be able to post data in these views. The data is partially complete here and there should be <num_expected> instances of <expected_response> in the response content """

        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.post(url, data=data)
        response_content = response.content.decode()

        assert response.status_code == 200
        assert len(list(re.finditer(expected_response,
                                    response_content))) is num_expected


    @pytest.mark.parametrize(
            "view_namespace_url, kwargs, data, expected_response, num_expected",
            [
                ('home:contact', {}, {'from_email': 'testemail.com', 'message':'test message body', 'subject':'test subject'},
                 'Enter a valid email', 1),
            ]
        )
    @pytest.mark.testing
    def test_home_invalid_data(
        self,
        view_namespace_url,
        kwargs,
        data,
        expected_response,
        num_expected,
        client
    ):
        """ Test clients are unregistered here but should be able to post data in these views. The data is complete here, but invalid and there should be <num_expected> instances of <expected_response> in the response content """

        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.post(url, data=data)
        response_content = response.content.decode()

        assert response.status_code == 200
        assert len(list(re.finditer(expected_response,
                                    response_content))) is num_expected
