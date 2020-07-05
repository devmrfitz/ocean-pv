from django.urls import path
from .views import (
    HowtoView,
    View,
    howto_relations_view,
    SelfQuestionView,
    RelationQuestionView
)
from .json_views import howto_relation_ajax

app_name = 'interactions'

urlpatterns = [

    path('howto/', HowtoView.as_view(), name='howto'),
    path('howto/relations/', howto_relations_view, name='howto-relations'),
    path('howto/relations/ajax/', howto_relation_ajax,
         name='howto-relations-ajax'),

    path('taketest/', SelfQuestionView.as_view(), name='taketest'),
    path('taketest/relations/<int:profile_pk>/<int:against>/', RelationQuestionView.as_view(),
         name='taketest-relations'),
    path('view/', View.as_view(), name='view')

]
