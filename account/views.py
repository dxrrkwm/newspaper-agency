from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import RedirectView

from account.forms import CreateRedactorForm, RedactorSearchForm
from account.models import Redactor


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    paginate_by = 6
    template_name = "newspaper/redactor_list.html"

    def get_context_data(self, **kwargs):
        context = super(RedactorListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", "")
        context["search_form"] = RedactorSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Redactor.objects.all()
        form = RedactorSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                username__startswith=form.cleaned_data["username"]
            )
        return queryset


class SignupView(generic.CreateView):
    model = Redactor
    form_class = CreateRedactorForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("account:redactor_list")


class UpdateRedactorView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    form_class = CreateRedactorForm
    template_name = "newspaper/redactor_detail.html"
    success_url = reverse_lazy("account:redactor_list")


class RedirectToLoginView(RedirectView):
    url = reverse_lazy("login")

