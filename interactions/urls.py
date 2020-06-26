from django.urls import path
from interactions.views import (
    HowtoView,
    View,
    howto_relations_view,
    SelfQuestionView,
    RelationQuestionView
)

app_name = 'interactions'

urlpatterns = [

    path('howto/', HowtoView.as_view(), name='howto'),
    path('howto/relations/', howto_relations_view, name='howto-relations'),
    path('taketest/', SelfQuestionView.as_view(), name='taketest'),
    path('taketest/relations/<int:pk>/', RelationQuestionView.as_view(),
         name='taketest-relations'),
    path('view/', View.as_view(), name='view')

]
