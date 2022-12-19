from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TReksadana(models.Model):
    name = models.CharField(max_length=1000)
    management = models.CharField(max_length=1000)
    custodian = models.CharField(max_length=1000)
    tipe_reksadana = models.CharField(max_length=1000)
    def __str__(self):
        return "{}".format(self.id)
    class Meta:
        verbose_name_plural = "Reksadana"

class TWatchlist(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    id_reksadana = models.ForeignKey(TReksadana, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return int(self.id_reksadana)  
    class Meta:
        verbose_name_plural = "Watchlist"
