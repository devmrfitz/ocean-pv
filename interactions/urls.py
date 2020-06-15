from django.urls import path
from interactions.views import (
    HowtoView,
    HowtoViewRelations,
    self_question_list_view,
    relation_question_list_view
)

app_name = 'interactions'

urlpatterns = [
    path('howto/', HowtoView.as_view(template_name='interactions/howto_self.html'), name='howto'),
    path('howto/relations/', HowtoViewRelations.as_view(), name='howto-relations'),
    path('taketest/', self_question_list_view, name='taketest'),
    path('taketest/relations/<int:pk>/', relation_question_list_view,
         name='taketest-relations'),
]
