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

    deadline = models.DateField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.project_name


class Staff(models.Model):
    firstname = models.CharField(
        max_length=25
    )

    lastname = models.CharField(
        max_length=60
    )

    def __str__(self):
        return self.firstname

class Content(models.Model):
    name = models.CharField(
        max_length=100,
        blank=True,
    )
    url = models.URLField(
        max_length=255,
    )
    outlet = models.CharField(
        max_length=100,
        blank=True,
    )
    author = models.CharField(
        max_length=75,
    )
    date = models.DateField(
        blank=True,
    )
    staff = models.ForeignKey(Staff)

    project = models.ForeignKey(
        Project,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class Metric(models.Model):
    name = models.CharField(
        max_length=50,
    )
    description = models.TextField(
        max_length=250,
    )

    def __str__(self):
        return self.name


class Note(models.Model):

    staff = models.ForeignKey(Staff)

    comment = models.TextField()

    content = models.ForeignKey(Content)

    def __str__(self):
        return self.comment
