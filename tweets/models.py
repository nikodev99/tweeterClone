from django.db import models

"""
This model is dedicated to a single tweet
"""


class Tweet(models.Model):
    # Maps to SQL data
    # id = models.AutoField(primary_key=true)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
