from __future__ import unicode_literals
from django.db import models

class Client(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Name of company',
    )

    contact = models.CharField(
        max_length=80,
        help_text='Primary contact at company',
        blank=True,
    )

    def __str__(self):
        return self.name

class Project(models.Model):
    project_name = models.CharField(
        max_length=200,
    )

    client=models.ForeignKey(Client)

    contact = models.CharField(
        max_length=80,
        blank=True
    )

    deadline = models.DateTimeField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.project_name
