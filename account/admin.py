from django.contrib import admin

from account.models import Redactor


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    list_display = ("years_of_experience", )
