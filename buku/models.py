from django.db import models

# Create your models here.
class Buku(models.Model):
    penulis = models.CharField(max_length=100)
    jenis_buku = models.CharField(max_length=100)
    judul = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    sinopsis = models.TextField()
    def __str__(self):
        return self.penulis
    class Meta:
        verbose_name_plural = "Buku"
