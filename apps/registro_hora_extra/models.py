from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)

    def _str_(self):
        return self.motivo
