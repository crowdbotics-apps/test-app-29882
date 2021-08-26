from django.conf import settings
from django.db import models


class CustomText(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=150,
    )


class HomePage(models.Model):
    "Generated Model"
    body = models.TextField()


class Profile_User(models.Model):
    "Generated Model"
    first_name = models.BigIntegerField()
    last_name = models.BigIntegerField()
    street_address = models.BigIntegerField()
    city = models.BigIntegerField()
    state = models.BigIntegerField()
    zip_code = models.BigIntegerField()
    activity_preferences = models.BigIntegerField()
