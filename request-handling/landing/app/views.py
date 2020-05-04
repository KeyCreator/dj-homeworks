from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    page = request.GET.get('from-landing')
    if page:
        counter_click[page.lower()] += 1
    return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    arg = request.GET.get('ab-test-arg', 'original')
    if arg.lower() == 'test':
        html_file = 'landing_alternate.html'
        counter_show[arg.lower()] += 1
    else:
        html_file = 'landing.html'
        counter_show['original'] += 1

    return render_to_response(html_file)


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    marker = request.GET.get('marker')
    counter_click[marker.lower()] += 1

    test_conversion = counter_click.get('test', 0) / counter_show['test'] if counter_show.get('test')\
        else f"The page test didn't display"
    original_conversion = counter_click.get('original', 0) / counter_show['original'] if counter_show.get('original')\
        else f"The page original didn't display"

    # Для вывода результат передайте в следующем формате:
    return render_to_response('stats.html', context={
        'test_conversion': test_conversion,
        'original_conversion': original_conversion,
    })
