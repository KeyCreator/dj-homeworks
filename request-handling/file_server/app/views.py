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
    path = settings.FILES_PATH
    files = os.listdir(path=path)
    files = map(lambda name: {'name': name,
                              'ctime': datetime.date.fromtimestamp(os.stat(os.path.join(path, name)).st_ctime),
                              'mtime': datetime.date.fromtimestamp(os.stat(os.path.join(path, name)).st_mtime)},
                files)
    pprint(list(files))

    context = {
        'files': list(files),
        'date': ''  # datetime.date(2020, 4, 25)  # Этот параметр необязательный
    }

    return render(request, template_name, context)


def file_content(request):
    # Реализуйте алгоритм подготавливающий контекстные данные для шаблона по примеру:
    return render(
        request,
        'file_content.html',
        context={'file_name': 'server01.01', 'file_content': 'File content!'}
    )

