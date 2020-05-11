from django import template


register = template.Library()

@register.filter
def float_to_currency(value):
    return "{:.02f} руб".format(value)


@register.filter
def add_unit(value, unit:str):
    return f'{value} {unit}'