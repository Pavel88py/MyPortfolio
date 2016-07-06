from __future__ import unicode_literals

from django.db import models

class Work(models.Model):
	organization = models.CharField(verbose_name='Organization', max_length=32)
	position = models.CharField(verbose_name='Position', max_length=16)

class Hobby(models.Model):
    name = models.CharField(verbose_name='Name', unique=True, max_length=32)