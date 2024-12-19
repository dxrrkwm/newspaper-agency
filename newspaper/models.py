from django.contrib.auth import get_user_model
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Topics"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="newspapers"
    )
    publishers = models.ManyToManyField(
        get_user_model(), related_name="newspapers"
    )

    def __str__(self):
        return f"{self.title} - {self.published_date}"
