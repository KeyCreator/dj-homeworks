from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара")
    rate = forms.IntegerField(label="Процентная ставка")
    months_count = forms.IntegerField(label="Срок кредита в месяцах")

    def clean_initial_fee(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        initial_fee = self.cleaned_data.get('initial_fee')
        if not initial_fee or initial_fee < 0:
            raise forms.ValidationError("Стоимость товара не может быть отрицательной")
        return initial_fee

    def clean_rate(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        rate = self.cleaned_data.get('rate')
        if not rate or rate < 0 or rate > 50 :
            raise forms.ValidationError("Значение процентной ставки должно быть от 0 до 50")
        return rate

    def clean_months_count(self):
        # валидация одного поля, функция начинающаяся на `clean_` + имя поля
        months_count = self.cleaned_data.get('months_count')
        if not months_count or months_count < 1 or months_count > 60 :
            raise forms.ValidationError("Максимальный срок кредида - 60 месяцев")
        return months_count

    def clean(self):
        # общая функция валидации
        return self.cleaned_data
