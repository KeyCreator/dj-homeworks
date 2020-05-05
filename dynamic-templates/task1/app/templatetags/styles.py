from django import template

register = template.Library()

@register.filter
def bgcolor(value):
    ''' Если инфляция за месяц была отрицательной (дефляция), то ячейка должна быть закрашена в зеленый.
    Если значение инфляции превысило 1%, то в красный.
    Должна быть реализована визуальная градация красного: от 1% до 2%, от 2% до 5%, от 5% и более
    (3 оттенка красного, визуально они должны быть различимы)
    '''
    value = float(value) if value else 0
    if value < 0:
        color = '#98FB98'
    elif value <= 1:
        color = '#FFFFFF'
    elif value <= 2:
        color = '#FFA07A'
    elif value <= 5:
        color = '#F08080'
    else:
        color = '#DC143C'

    return color