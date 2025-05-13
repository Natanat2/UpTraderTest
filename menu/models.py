from django.db import models
from django.urls import NoReverseMatch, reverse


class Menu(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    url = models.CharField(max_length=240, blank=True, help_text="Прямой URL или имя именованного URL")
    named_url = models.BooleanField(default=False, help_text="Отметьте, если это именованный URL")

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.url)
            except NoReverseMatch:
                return '#'
        return self.url
