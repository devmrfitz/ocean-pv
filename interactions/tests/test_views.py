from django.urls import resolve, reverse
import pytest

from interactions.models import SelfQuestion


class TestInteractionsGetMethod:

    @pytest.mark.parametrize(
        "view_namespace_url, kwargs, template_name, response_content",
        [
            ('interactions:howto', {}, 'interactions/howto_self.html',
             'You are not logged in, you will be redirected to login'),
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
             {'pk': 1}, 'interactions/questions.html', ''),
            ('interactions:howto-relations', {}, 'interactions/howto_relations.html',
             ''),
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
             'there are no questions in the database'),
            ('interactions:taketest-relations', {'pk': 1}, 'interactions/error.html',
             'there are no questions in the database'),
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
             'there are no questions in the database', 'SelfQuestion'),
            ('interactions:taketest-relations', {'pk': 1}, 'interactions/questions.html',
             'there are no questions in the database', 'RelationQuestion'),
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
            create_questions
    ):
        """ Test clients are registered here and they should be able to access these views, and there are questions in the database and they should be displayed properly """

        create_questions(question_model)
        user, client = login_user()
        url = reverse(view_namespace_url, kwargs=kwargs if kwargs else None)
        response = client.get(url)

        assert response.status_code == 200
        assert template_name in [t.name for t in response.templates]
        assert response_content.encode() not in response.content


class TestInteractionsPostMethod:
    pass
