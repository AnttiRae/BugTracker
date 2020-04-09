from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
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
    created_at = models.DateTimeField(default=timezone.now)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return '%s by %s' % (self.title, self.reported_by)

class Comment(models.Model):
    message = models.CharField(max_length=512)
    bug = models.ForeignKey(Bug, on_delete=models.CASCADE)
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)
    voters = ArrayField(models.CharField(max_length=150), default=list)

    def __str__(self):
        return '%s - %s' % (self.created_at, self.commented_by)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=512, blank=True)
    image = models.FileField(upload_to='images/', null=True, verbose_name='kuva')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()