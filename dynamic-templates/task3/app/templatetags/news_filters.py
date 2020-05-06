from django import template
from datetime import datetime
import re


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
def format_score(value, default=None):
    ''' Рейтинг меньше -5, пишет "все плохо"
        Рейтинг от -5 до 5 – "нейтрально"
        Рейтинг больше 5 – "хорошо"
        Если поле score отсутствует, то рендерится дефолтное значение, которое передается в качестве параметра фильтра
    '''
    if not value:
        return default

    score = int(value)
    if score < -5:
        value = "все плохо"
    elif score <= 5:
        value = "нейтрально"
    else:
        value = "хорошо"

    return value

@register.filter
def format_num_comments(value):
    ''' Если комментариев 0, пишется "Оставьте комментарий"
        От 0 до 50, пишем число комментариев
        Больше 50, пишем "50+"
    '''
    # Ваш код
    count = int(value)
    if not count:
        value = "Оставьте комментарий"
    elif count > 50:
        value = "50+"

    return value

@register.filter
def format_selftext(value, count=0):
    '''Оставляет count первых и count последних слов, между ними должно быть троеточие.
    count задается параметром фильтра.
    Пример c count = 5: "Hi all sorry if this ... help or advice greatly appreciated."
    Знаки препинания остаются, обрезаются только слова.
    '''
    # return value
    if not count:
        return value

    pattern = re.compile('\w+')
    matches = pattern.findall(value)
    print(f'Длина текста {len(matches)}')

    if len(matches) > count * 3:
        pattern1 = re.compile(r'\A(\W*\w+\W+){'+str(count)+'}')
        pattern2 = re.compile(r'(\W+\w*\W*){'+str(count)+'}\Z')
        value = f'{pattern1.search(value).group(0)} ... {pattern2.search(value).group(0)}'

    return value
