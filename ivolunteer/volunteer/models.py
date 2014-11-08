from django.db import models

# Create your models here.

class Volunteer(models.Model):
    volunteer_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.volunteer_name

class Organisation(models.Model):
    organisation_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.organisation_name
