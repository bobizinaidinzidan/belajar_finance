from django.db import models

# Create your models here.
class TypeBerita(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Type"

class TBerita(models.Model):
    author = models.CharField(null=True, max_length=1000)
    title = models.CharField(max_length=1000, null=True)
    tipe_berita = models.ForeignKey(TypeBerita, on_delete=models.CASCADE, blank=True, null=True)
    description = models.CharField(max_length=1000, null=True)
    url = models.URLField(max_length=1000, null=True)
    urlToImage = models.URLField(max_length=1000,null=True)
    publishedAt = models.DateTimeField(null=True)
    content = models.TextField(null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Berita"

