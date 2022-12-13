from django.db import models

# Create your models here.
class TReksadana(models.Model):
    name = models.CharField(max_length=1000)
    management = models.CharField(max_length=1000)
    custodian = models.CharField(max_length=1000)
    tipe_reksadana = models.CharField(max_length=1000)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Reksadana"
