from django.urls import path

from account.views import RedactorListView, SignupView, UpdateRedactorView

app_name = "account"

urlpatterns = [
    path("redactors/", RedactorListView.as_view(), name="redactor_list"),
    path("signup/", SignupView.as_view(), name="signup"),
    path("update/<int:pk>", UpdateRedactorView.as_view(), name="redactor-update"),
]