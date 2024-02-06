from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100, null=True)
    url = models.CharField(max_length=200, null=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )
    named_url = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name
