from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class TGroup(models.Model):
    name = models.CharField(max_length=1000)
    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        verbose_name_plural = "Group"
class TAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(TGroup, on_delete=models.CASCADE)
    def __str__(self):
        return "{} - {}".format(self.user, self.group)
    class Meta:
        verbose_name_plural = "Account"