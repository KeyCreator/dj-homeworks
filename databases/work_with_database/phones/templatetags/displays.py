from django import template


register = template.Library()

@register.filter
def bool_to_str(value):
    return 'Есть' if value else 'Отсутствует'