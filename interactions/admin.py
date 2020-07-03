from django.contrib import admin
from interactions.models import (
    SelfAnswerGroup,
    RelationAnswerGroup
)


admin.site.site_header = 'ocean-pv administration'


@admin.register(SelfAnswerGroup)
class SelfAnswerGroupAdmin(admin.ModelAdmin):
    readonly_fields = ['return_formatted_json']
    fieldsets = [
        ('User Information', {
            'fields': ['self_user_profile']
        }),
        ('Answer and questions', {
            'fields': ['accuracy', 'return_formatted_json']
        })
    ]


@admin.register(RelationAnswerGroup)
class RelationAnswerGroupAdmin(SelfAnswerGroupAdmin):
    pass
