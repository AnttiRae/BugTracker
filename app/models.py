from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Bug(models.Model):
    PRIORITIES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    id = models.AutoField(primary_key=True)
    fixed = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    priority = models.CharField(max_length=10, choices=PRIORITIES)
    description = models.CharField(max_length=10000)
    created_at = models.DateField(default=timezone.now)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return '%s by %s' % (self.title, self.reported_by)

class Comment(models.Model):
    message = models.CharField(max_length=512)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=timezone.now)
    score = models.IntegerField(default=0)

    def __str__(self):
        return '%s - %s' % (self.created_at, self.commented_by)