from django.urls import path

from newspaper.views import NewspaperListView, NewspaperDetailView, NewspaperCreateView, NewspaperUpdateView, \
    NewspaperDeleteView, TopicListView, TopicUpdateView, TopicDeleteView

app_name = 'newspaper'

urlpatterns = [
    path("", NewspaperListView.as_view(), name="index"),
    path("<int:pk>/", NewspaperDetailView.as_view(), name="detail"),
    path("create/", NewspaperCreateView.as_view(), name="create"),
    path("<int:pk>/update/", NewspaperUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", NewspaperDeleteView.as_view(), name="delete"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/update/<int:pk>/", TopicUpdateView.as_view(), name="update-topic"),
    path("topics/delete/<int:pk>/", TopicDeleteView.as_view(), name="delete-topic"),
]
