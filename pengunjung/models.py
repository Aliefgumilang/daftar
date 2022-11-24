from django.db import models

# Create your models here.
class Kategori(models.Model):
    nama = models.CharField(max_length = 40)
    def __str__(self):
        return self.nama

class Daftar(models.Model):
    nama = models.CharField(max_length = 50)
    deskripsi = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.nama