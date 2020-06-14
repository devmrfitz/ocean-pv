from django.urls import resolve, reverse
import pytest

from interactions.models import SelfQuestion


class TestInteractionsGetMethod:

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, template_name, response_content",
        [
            ('interactions:howto', {}, 'interactions/howto.html',
             'Since you are not logged in, you will be redirected to the login page '),
        ]
    )
    def test_interactions_views(
        self,
        view_namespace_url,
        kwargs,
        template_name,
        response_content,
        client
    ):
        """ Test clients are unregistered here but should be able to access these views """

        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.get(url)

        assert response.status_code == 200
        assert template_name in [t.name for t in response.templates]
        assert response_content.encode() in response.content

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, template_name, response_content",
        [
            ('interactions:taketest', {}, 'interactions/questions.html', ''),
            ('interactions:taketest-relations',
             {}, 'interactions/questions.html', '')
        ]
    )
    def test_interactions_views_unregistered_redirect(
        self,
        view_namespace_url,
        kwargs,
        template_name,
        response_content,
        client
    ):
        """ Test clients are unregistered here and shouldn't be able to access these views """

        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.get(url)

        assert response.status_code == 302
        assert template_name not in [t.name for t in response.templates]
        assert response_content.encode() in response.content

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, template_name, response_content",
        [
            ('interactions:taketest', {}, 'interactions/error.html',
             'There are no questions in the database'),
            ('interactions:taketest-relations', {}, 'interactions/error.html',
             'There are no questions in the database'),
        ]
    )
    def test_interactions_views_registered_empty(
            self,
            view_namespace_url,
            kwargs,
            template_name,
            response_content,
            login_user,
    ):
        """ Test clients are registered here and they should be able to access these views, but there are no questions in the database and should get an error saying so. """

        user, client = login_user()
        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.get(url)

        assert response.status_code == 200
        assert template_name in [t.name for t in response.templates]
        assert response_content.encode() in response.content

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, template_name, response_content, question_model",
        [
            ('interactions:taketest', {}, 'interactions/questions.html',
             'Are you sometimes shy and inhibited?', 'SelfQuestion'),
            ('interactions:taketest-relations', {}, 'interactions/questions.html',
             'They are relaxed and handle stress well', 'RelationQuestion'),
        ]
    )
    @pytest.mark.testing
    def test_interactions_views_registered_non_empty(
            self,
            view_namespace_url,
            kwargs,
            template_name,
            response_content,
            login_user,
            question_model,
            create_self_questions,
            create_relation_questions
    ):
        """ Test clients are registered here and they should be able to access these views, and there are questions in the database and they should be displayed properly """

        user, client = login_user()
        if question_model == 'SelfQuestion':
            create_self_questions()
        else:
            create_relation_questions()
        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.get(url)

        assert response.status_code == 200
        assert template_name in [t.name for t in response.templates]
        assert response_content.encode() in response.content
