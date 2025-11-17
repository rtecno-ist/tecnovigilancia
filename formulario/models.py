from django.db import models

class Incidente(models.Model):

    AREA_CHOICES = [
        ('recepcion', 'Recepción'),
        ('almacenamiento', 'Almacenamiento'),
        ('despacho', 'Despacho'),
        ('transporte', 'Transporte'),
        ('uso', 'Uso'),
    ]

    OCURRIDO_CHOICES = [
        ('falla_calidad', 'Falla de calidad (envase, etiqueta, aspecto, vencimiento)'),
        ('incidente', 'Incidente (no causó daño, pero pudo causar)'),
        ('evento_adverso', 'Evento adverso (causó daño o riesgo de daño)'),
        ('casi_evento', 'Casi evento (error detectado a tiempo)'),
    ]

    ACCIONES_CHOICES = [
        ('aisle', 'Aislé el producto'),
        ('avise', 'Avisé a jefatura / Responsable de Tecnovigilancia'),
        ('otro', 'Otro'),
    ]

    # Código autogenerado
    codigo = models.CharField(max_length=20, unique=True, blank=True)

    # Datos Generales
    nombre = models.CharField(max_length=200)
    area = models.CharField(max_length=20, choices=AREA_CHOICES)
    fecha = models.DateField()
    hora = models.TimeField()

    # Dispositivo Médico
    nombre_dispositivo = models.CharField(max_length=200)
    lote = models.CharField(max_length=100)
    proveedor = models.CharField(max_length=200)

    # Qué ocurrió
    que_ocurrio = models.CharField(max_length=20, choices=OCURRIDO_CHOICES)

    # Descripción
    descripcion = models.TextField()

    # Acciones tomadas
    acciones = models.JSONField(default=list)  # lista con los checks marcados

    # Adjuntos
    archivo_adjunto = models.FileField(upload_to="adjuntos/", blank=True, null=True)

    def save(self, *args, **kwargs):
        # Generar código tipo TV-0001
        if not self.codigo:
            ultimo = Incidente.objects.order_by('-id').first()
            numero = (ultimo.id + 1) if ultimo else 1
            self.codigo = f"TV-{numero:04d}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
