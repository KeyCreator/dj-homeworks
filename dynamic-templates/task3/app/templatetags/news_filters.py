from django import template
from datetime import datetime
import math


register = template.Library()


@register.filter
def format_date(value):
    # Ваш код
    creation_time = datetime.fromtimestamp(value)
    current_time = datetime.utcnow()
    difference = (current_time - creation_time).seconds
    difference = difference/60

    if difference <= 10:
        value = 'только что'
    elif difference < 60:
        value = 'менее часа назад'
    elif difference <= 24 * 60:
        value = f'{int(difference/60)} часов назад'
    else:
        value = creation_time.date()

    return value


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value):
    return

@register.filter
def format_num_comments(value):
    # Ваш код
    return value



