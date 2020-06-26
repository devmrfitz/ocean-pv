from django.urls import reverse, resolve
import pytest

from interactions.views import (
    HowtoView,
    View,
    relation_question_list_view,
    self_question_list_view,
    howto_relations_view
)


@pytest.mark.unittest
@pytest.mark.parametrize(
    "reverse_url,kwargs ,resolve_url, view_func",
    [
        # Func-based Views
        ('interactions:taketest', {}, '/interactions/taketest/',
         self_question_list_view),
        ('interactions:taketest-relations', {'pk': 1},
         '/interactions/taketest/relations/1/', relation_question_list_view),

        # Class-based Views
        ('interactions:howto', {}, '/interactions/howto/', HowtoView),
        ('interactions:howto-relations', {},
         '/interactions/howto/relations/', howto_relations_view),
        ('interactions:view', {}, '/interactions/view/', View),
    ]
)
def test_urls_interactions(
    return_views,
    kwargs,
    reverse_url,
    resolve_url,
    view_func
):
    """ Test app-> interactions urls """

    reverse_view, resolve_view = return_views(reverse_url, resolve_url, kwargs)

    try:
        assert reverse_view.func == view_func
        assert resolve_view.func == view_func
    except (AttributeError, AssertionError):
        assert reverse_view.func.view_class == view_func
        assert resolve_view.func.view_class == view_func


if __name__ == '__main__':
    pytest.main()
