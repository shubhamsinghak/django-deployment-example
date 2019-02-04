from django import template
register = template.Library()

@register.filter
def cut(value,arg):
    """
    This cuts all values of "arg" from the string!
    """
    return value.replace(arg,'')
