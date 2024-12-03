from django.contrib import admin

from newspaper.models import Newspaper, Topic


@admin.register(Newspaper)
class NewspaperAdmin(admin.ModelAdmin):
    pass

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
