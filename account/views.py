from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from account.forms import CreateRedactorForm
from account.models import Redactor


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor


class SignupView(generic.CreateView):
    model = Redactor
    form_class = CreateRedactorForm
    template_name = 'registration/signup.html'


class UpdateRedactorView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = CreateRedactorForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('account:redactor_list')
