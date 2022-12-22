from django.db import models

# Create your models here.
class TBerita(models.Model):
    author = models.CharField(null=True, max_length=1000)
    title = models.CharField(max_length=1000, null=True)
    tags = models.CharField(max_length=1000, null=True)
    description = models.TextField(null=True)
    url = models.URLField(max_length=1000, null=True)
    urlToImage = models.URLField(max_length=1000,null=True)
    publishedAt = models.DateTimeField(null=True)
    def __str__(self):
        return "{}".format(self.title)
    class Meta:
        verbose_name_plural = "Berita"

