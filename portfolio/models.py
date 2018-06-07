from django.db import models
from django.utils import timezone

import datetime
# Create your models here.


class Pics(models.Model):
    title = models.CharField(max_length=200)
    pics = models.FileField(null=False, blank=False)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'