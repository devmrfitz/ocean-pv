from django import template


register = template.Library()


@register.filter(name='zip_lists')
def zip_lists(list1, list2):
    if len(list1)!=len(list2):
        raise template.TemplateSyntaxError(
        'Only lists of equal length can be zipped'
        )
    return zip(list1, list2)
