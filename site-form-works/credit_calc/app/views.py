from django.shortcuts import render

from .forms import CalcForm


def calc_view(request):
    template = "app/calc.html"
    context = {}

    if request.method == 'GET':
        form = CalcForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            common_result = data['initial_fee'] + data['initial_fee'] * data['rate']
            result = common_result / data['months_count']
            print('Результат = ', result)
            context['result'] = result
            context['common_result'] = common_result
        context['form'] = form
    else:
        context['form'] = CalcForm

    return render(request, template, context)
