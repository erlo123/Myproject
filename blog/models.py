import datetime
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    title_text = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    head_text = models.CharField(max_length=400)

    def __str__(self):
        return self.title_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        was_published_recently.admin_order_field = 'pub_date'
        was_published_recently.boolean = True
        was_published_recently.short_description = 'Published recently?'

class Single(models.Model):
    title = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.content_text

class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.user