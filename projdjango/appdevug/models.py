from django.db import models

# Create your models here.
class Tutorial(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()  # Cambiado de CharField() a TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)  # Cambiado auto_now_add a auto_now
    autor_uid = models.CharField(max_length=255)  # Agregado max_length
    autor_nombre = models.CharField(max_length=255)
    autor_foto_url = models.URLField(blank=True, null=True)  # Agregado blank y null

    class Meta:
        verbose_name = "Tutorial"
        verbose_name_plural = "Tutoriales"
        ordering = ['-fecha_creacion']

    def __str__(self):  # Movido fuera de Meta
        return f"{self.titulo} por {self.autor_nombre}"
        
class Reaccion(models.Model):
    TIPOS_EMOJI = [
        ('like', 'me gusta'),
        ('wow', 'asombro'),
        ('love', 'me encanta'),
    ]

    usuario_uid = models.CharField(max_length=255)  # Agregado max_length
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name='reacciones')
    emoji = models.CharField(max_length=20, choices=TIPOS_EMOJI)
    fecha_reaccion = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Reacción"
        verbose_name_plural = "Reacciones"
        unique_together = ('usuario_uid', 'tutorial', 'emoji')

    def __str__(self):  # Movido fuera de Meta y corregido typo
        return f"{self.usuario_uid} reaccionó con {self.emoji} al tutorial {self.tutorial.titulo}"