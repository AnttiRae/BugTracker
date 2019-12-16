from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Bug(models.Model):
    fixed = models.BooleanField(default=False)
    priority = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateField(default=timezone.now)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.description, self.reported_by)
