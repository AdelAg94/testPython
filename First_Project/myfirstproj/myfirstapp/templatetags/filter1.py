from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value, arg):
    """
    This will take any argument and replace it with empty string
    """
    return value.replace(arg, '')