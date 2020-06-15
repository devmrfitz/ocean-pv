from django.urls import resolve, reverse
import pytest


class TestHomeGetMethod:

    @pytest.mark.parametrize(
        "view_namespace_url, args, template_name",
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
        args,
        template_name,
        client
    ):
        """ Test clients are unregistered here but should be able to access these views """
        
        url = reverse(view_namespace_url, args=args if args else None)
        response = client.get(url)

        assert response.status_code == 200
        assert template_name in [t.name for t in response.templates]
