from django.contrib.auth.forms import UserCreationForm

from account.models import Redactor


class CreateRedactorForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + ('years_of_experience', 'username', 'email', 'first_name', 'last_name')
