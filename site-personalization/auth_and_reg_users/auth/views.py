from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import SignupForm
from .models import CustomUser
# from django.http import HttpResponseRedirect
# from django.views.generic.base import View
# from django.contrib.auth import login, logout


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return render(request, self.template_name)


class SignupFormView(FormView):
    template_name = 'signup.html'
    form_class = SignupForm # #UserCreationForm
    success_url = '/login/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data)
            user = CustomUser.objects.create_user(username=form_data['username'], password=form_data['password1'])
            user.is_staff = True
            user.save()

        return redirect('/')


    # def form_valid(self, form):
    #     data=form.cleaned_data
    #     form.save()
    #     return super(SignupFormView, self).form_valid(form)
    #
    # def form_invalid(self, form):
    #     return super(SignupFormView, self).form_invalid(form)
