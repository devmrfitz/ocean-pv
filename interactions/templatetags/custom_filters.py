from django import template


register = template.Library()


@register.filter(name='zip_lists')
def zip_lists(list1, list2):
    if len(list1) != len(list2):
        raise template.TemplateSyntaxError(
            'Only lists of equal length can be zipped'
        )
    return zip(list1, list2)


@register.filter(name='make_subsets')
def make_subsets(data, size: int) -> list:
    """ Creates subsets out of ``data``, each subset have ``size``
    elements. """

    subset_list = []
    if type(data) is list:
        subset = []
        return ('list')
    elif type(data) is dict:
        subset = {}
        while True:
            key, value = data.popitem()
            subset.update({key.capitalize(): value})
            if len(subset) == size:
                subset_list.append(subset)
                subset = {}
            if not data:
                subset_list.append(subset)
                break
    print(subset_list, len(subset_list))

    return subset_list
