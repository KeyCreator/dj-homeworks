import datetime
import os
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from pprint import pprint

def index(request):
    return redirect(reverse(file_list))


def file_list(request):
    template_name = 'index.html'
    
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    dt_format = lambda time: datetime.date.fromtimestamp(time)

    dt = request.GET.get('date')
    print(f'Параметр date={dt}')
    if dt:
        dt = datetime.datetime.strptime(dt, '%Y-%m-%d').date()
        print(f'Параметр date после конвертации={dt} type {type(dt)}')

    path = settings.FILES_PATH
    files = os.listdir(path=path)
    files = map(lambda name: {'name': name,
                              'ctime': dt_format(os.stat(os.path.join(path, name)).st_ctime),
                              'mtime': dt_format(os.stat(os.path.join(path, name)).st_mtime),
                              'date_type': type(dt_format(os.stat(os.path.join(path, name)).st_ctime))},

                files)
    files = list(files)
    pprint(files)
    context = {
        'files': files,
        'date':  dt  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request, name):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    path = os.path.join(settings.FILES_PATH, name)

    with open(path, "r") as file:
        reader = file.read()

    content = reader
    print(content)
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': content}
    )

