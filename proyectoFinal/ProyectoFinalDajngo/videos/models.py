from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="videos")
    nombre = models.CharField(max_length=200)
    extension = models.CharField(max_length=10)
    tamaño = models.FloatField(help_text="Tamaño en MB")
    archivo = models.FileField(upload_to="videos/")
    creado_en = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.titulo
