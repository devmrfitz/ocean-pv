from django.contrib import admin
from interactions.models import (
    SelfQuestion,
    SelfAnswerGroup,
    Average,
    RelationQuestion,
    UserAnswerChoice,
    RelationAnswerChoice,
    RelationAnswerGroup
)

admin.site.register(SelfQuestion)
# admin.site.register(Average)
admin.site.register(RelationQuestion)
admin.site.register(SelfAnswerGroup)
admin.site.register(RelationAnswerGroup)
