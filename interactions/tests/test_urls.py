from django.urls import reverse, resolve
import pytest

from interactions.views import (
    HowtoView,
    relation_question_list_view,
    self_question_list_view
)


@pytest.mark.parametrize(
    "reverse_url,kwargs ,resolve_url, view_func, class_based",
    [
        # Func-based Views
        ('interactions:taketest', {}, '/interactions/taketest/',
         self_question_list_view, False),
        ('interactions:taketest-relations', {},
         '/interactions/taketest/relations/', relation_question_list_view, False),

        # Class-based Views
        ('interactions:howto', {}, '/interactions/howto/', HowtoView, True),
        ('interactions:howto-relations', {}, '/interactions/howto/relations/', HowtoView, True),
    ]
)
@ pytest.mark.django_db
def test_urls_interactions(
    return_views,
    kwargs,
    reverse_url,
    resolve_url,
    view_func,
    class_based
):
    """ Test app-> interactions urls """

    reverse_view, resolve_view = return_views(reverse_url, resolve_url, kwargs)

    if not class_based:
        assert reverse_view.func == view_func
        assert resolve_view.func == view_func
    else:
        assert reverse_view.func.view_class == view_func
        assert resolve_view.func.view_class == view_func
