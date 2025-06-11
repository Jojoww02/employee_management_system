from django.db import models

class Employee(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    jabatan = models.CharField(max_length=50)
    alamat = models.TextField()
    tanggal_bergabung = models.DateField()

    def __str__(self):
        return self.nama
