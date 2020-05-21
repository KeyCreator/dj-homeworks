from django import forms
from .models import Review, Product


class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea, label='Отзыв')

    class Meta(object):
        model = Review
        exclude = ('id', 'product')

    # def clean(self):
    #     cleaned_data = self.cleaned_data

        # if Review.objects.filter(product=1).count() > 0:
        #     raise forms.ValidationError("Вы уже оставили один отзыв")

        # return cleaned_data
