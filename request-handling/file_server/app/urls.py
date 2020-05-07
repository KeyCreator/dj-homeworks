from datetime import datetime
from django.urls import path, register_converter
from app.views import index, file_list, file_content

# Определите и зарегистрируйте конвертер для определения даты в урлах и наоборот урла по датам
class DateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, '%Y-%m-%d').date()

    def to_url(self, value: datetime) -> str:
        return value.strftime('%Y-%m-%d')


register_converter(DateConverter, 'datetime')


urlpatterns = [
    # Определите схему урлов с привязкой к отображениям .views.file_list и .views.file_content
    path('', index, name='index'),
    path('files/', file_list, name='file_list'),
    path('files/<datetime:date>/', file_list, name='file_list'),    # задайте необязательный параметр "date"
                                      # для детальной информации смотрите HTML-шаблоны в директории templates
    path('content/<name>/', file_content, name='file_content'),
]
