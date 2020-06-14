import pytest
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views

from graphs.views import (
    single_result_view,
    multiple_result_view
)


@pytest.mark.parametrize(
    "reverse_url, kwargs, resolve_url, view_func, class_based",
    [
        ('graphs:multiple_results', {},
         '/graphs/multiple/', multiple_result_view, False),
        ('graphs:single_result', {'pk': 30},
         '/graphs/30/', single_result_view, False),
    ]
)
def test_home_urls(
    return_views,
    reverse_url,
    kwargs,
    resolve_url,
    view_func,
    class_based
):
    """ Test app-> graphs urls """

    reverse_view, resolve_view = return_views(
        reverse_url, resolve_url, kwargs)

    if not class_based:
        assert reverse_view.func == view_func
        assert resolve_view.func == view_func
    else:
        assert reverse_view.func.view_class == view_func
        assert resolve_view.func.view_class == view_func
