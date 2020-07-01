from django.urls import resolve, reverse
import pytest

from graphs.views import (
    single_result_view,
    multiple_result_view,
)


@pytest.mark.unittest
class TestGraphsViewsGetMethod:

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, template_name",
        [
            ('graphs:multiple_results', {}, 'graphs/multiple_results.html'),
        ]
    )
    def test_graphs_views_unregistered(
        self,
        view_namespace_url,
        kwargs,
        template_name,
        login_user
    ):
        """ Test clients are unregistered here and they should return temporary redirect url """
        user, client = login_user()
        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.get(url)

        assert response.status_code == 200
        assert template_name in [t.name for t in response.templates]

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, template_name, mode",
        [
            ('graphs:single_result', {'pk': 1},
             'graphs/individual_result.html', 'self'),
        ]
    )
    def test_graphs_views_registered(
        self,
        view_namespace_url,
        kwargs,
        template_name,
        mode,
        login_user,
        interactions_wrapper
    ):
        """ Test clients are registered here and they should be able to access these views """

        user, client = login_user()
        interactions_wrapper(user, mode)
        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.get(url)

        assert response.status_code == 200
        assert template_name in [t.name for t in response.templates]


if __name__ == '__main__':
    pytest.main()
