from django.urls import path
from interactions.views import (
    HowtoView,
    HowtoViewRelations,
    self_question_list_view,
    relation_question_list_view,
    howto_relations_view
)

app_name = 'interactions'

urlpatterns = [
    path('howto/', HowtoView.as_view(), name='howto'),
    path('howto/relations/', howto_relations_view, name='howto-relations'),
    path('taketest/', self_question_list_view, name='taketest'),
    
    path('taketest/relations/<int:pk>/', relation_question_list_view,
         name='taketest-relations'),
    
]
