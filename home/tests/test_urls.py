import pytest
from django.urls import reverse, resolve

from home.views import (
    HomeView,
    ContactView,
    ContactDoneView, 
    ResourcesView
)


@pytest.mark.parametrize(
    "reverse_url, kwargs, resolve_url, view_func, class_based",
    [
        ('home:home', {}, '/', HomeView, True),
        ('home:contact', {}, '/contact/', ContactView, True),
        ('home:contact-done', {}, '/contact/done/', ContactDoneView, True),
        ('home:resources', {}, '/resources/', ResourcesView, True),
    ]
)
def test_home_urls(
    return_views,
    reverse_url,
    kwargs,
    resolve_url,
    view_func,
    class_based,
):
    """ Test app-> home urls """

    reverse_view, resolve_view = return_views(reverse_url, resolve_url, kwargs)

    if not class_based:
        assert reverse_view.func == view_func
        assert resolve_view.func == view_func
    else:
        assert reverse_view.func.view_class == view_func
        assert resolve_view.func.view_class == view_func
