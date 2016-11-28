from django import template

register = template.Library()


@register.filter
def lookup(list_name, key):
    '''
        This filter use for list indexing.
        Ex. list_name|lookup:var
    '''
    return list_name[key]
