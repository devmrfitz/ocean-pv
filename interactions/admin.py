from django.contrib import admin
from interactions.models import (
    SelfAnswerGroup,
    RelationAnswerGroup
)


admin.site.site_header = 'ocean-pv administration'


@admin.register(SelfAnswerGroup)
class SelfAnswerGroupAdmin(admin.ModelAdmin):
    readonly_fields = ['return_formatted_json', 'scores', 'accuracy']
    fieldsets = [
        ('User Information', {
            'fields': ['self_user_profile']
        }),
        ('Answer and questions', {
            'fields': ['accuracy', 'scores', 'return_formatted_json']
        })
    ]


@admin.register(RelationAnswerGroup)
class RelationAnswerGroupAdmin(SelfAnswerGroupAdmin):
    pass
