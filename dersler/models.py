from django.db import models
from django.contrib.auth.models import User

class Dersler(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_id = models.CharField(max_length=100)
    begeni_sayisi = models.PositiveBigIntegerField(default=0)
    is_active=models.BooleanField(default=False)
    kategori= models.TextField()
    

    def __str__(self):
        return self.title

class Yorum(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    ders = models.ForeignKey(Dersler, on_delete=models.CASCADE)
    icerik = models.TextField()
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.kullanici.username} - {self.ders.title} - {self.tarih}"


class KullaniciBegeni(models.Model):
    kullanici = models.ForeignKey(User, on_delete=models.CASCADE)
    ders = models.ForeignKey(Dersler, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('kullanici', 'ders',)
    
    def __str__(self):
        return f"{self.kullanici.username} - {self.ders.title}"

class CanliDersler(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_id = models.CharField(max_length=100)

    def __str__(self):
        return self.title