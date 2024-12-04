from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import RedirectView

from account.forms import CreateRedactorForm
from account.models import Redactor


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    context_object_name = 'redactors'
    template_name = 'newspaper/redactor_list.html'
    success_url = reverse_lazy('account:redactor_list')


class SignupView(generic.CreateView):
    model = Redactor
    form_class = CreateRedactorForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('account:redactor_list')


class UpdateRedactorView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = CreateRedactorForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('account:redactor_list')


class RedirectToLoginView(RedirectView):
    url = reverse_lazy('login')
