from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Type"


class Reksadana(models.Model):
    name = models.CharField(max_length=200)
    management = models.CharField(max_length=200)
    custodian = models.CharField(max_length=200)
    type = models.ForeignKey(Type, on_delete=models.CASCADE,blank= True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Reksadana"
