from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver


class UploadFileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=False, null=False)
    descriptions = models.TextField(max_length=1000, blank=True, null=True)
    file = models.FileField(upload_to='upload/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


@receiver(post_save, sender=UploadFileModel)
def create_expire_time(sender, instance, created, **kwargs):
    if created:
        ExpireTime.objects.create(file=instance)


class ExpireTime(models.Model):
    file = models.OneToOneField(UploadFileModel, on_delete=models.CASCADE)
    exp_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + ' ' + str(self.exp_time)
