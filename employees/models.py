from django.db import models

class Employee(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    jabatan = models.CharField(max_length=50)
    alamat = models.TextField()
    tanggal_bergabung = models.DateField()
    total_gaji = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    tanggal_lahir = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nama
