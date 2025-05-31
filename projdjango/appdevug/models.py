from django.db import models
from django.db import models

# Create your models here.
class Tutorial(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.CharField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificación = models.DateTimeField(auto_now_add=True)
    autor_uid = models.CharField() #UID de Firebase
    autor_nombre = models.CharField(max_length=255)
    autor_foto_url = models.URLField()

    class Meta:
        verbose_name = "Tutorial"
        verbose_name_plural = "Tutoriales"
        ordering = ['-fecha_creacion']

        def __str__(self):
            return f"{self.titulo} por {self.autor_nombre}"
        
class Reaccion(models.Model):
    TIPOS_EMOJI = [
        ('like', 'me gusta'),
        ('wow', 'asombro'),
        ('love', 'me encanta'),
    ]

    usuario_uid = models.CharField() # UID de Firebase
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name='reacciones')
    emoji = models.CharField(max_length=20, choices=TIPOS_EMOJI)
    fecha_reaccion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Reacción"
        verbose_name_plural = "Reacciones"
        unique_together = ('usuario_uid', 'tutorial', 'emoji')

        def __str__(self):
            return f"{self.usuario_uid} reacionó con {self.tipo_emoji} al tutorial {self.tutorial.titulo}"