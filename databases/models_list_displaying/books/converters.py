from datetime import datetime


class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    def to_python(self, value: str) -> datetime:
        return datetime.strptime(value, '%Y-%m-%d').date()

    def to_url(self, value: datetime) -> str:
        return value.strftime('%Y-%m-%d')