from django.contrib import admin
from interactions.models import (
    SelfAnswerGroup,
    RelationAnswerGroup 
)

# admin.site.register(Average)
admin.site.register(SelfAnswerGroup)
admin.site.register(RelationAnswerGroup)
# admin.site.register(RelationAnswerChoice)
# admin.site.register(UserAnswerChoice)