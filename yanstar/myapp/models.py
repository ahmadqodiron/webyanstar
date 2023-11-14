from django.db import models

class Design(models.Model):
  Nama_Desing = models.CharField(max_length=255)
  Tanggal = models.DateField()
 
  def __str__(self):
    return f"{self.Nama_Desing}"

class Contact(models.Model):
  Nama = models.CharField(max_length=255)
  Email = models.CharField(max_length=255)
  No_Hp = models.IntegerField(max_length=255)
  IG = models.CharField(max_length=255)
 
  def __str__(self):
    return f"{self.Nama} {self.Email}"    