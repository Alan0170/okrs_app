from django.db import models


class Integrante(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)

    def __str__(self):
        return self.nome


class Okr(models.Model):
    integrante = models.ForeignKey(Integrante, on_delete=models.CASCADE)
    objetivo = models.CharField(max_length=255)
    resultado_1 = models.CharField(max_length=255)
    resultado_2 = models.CharField(max_length=255, blank=True)
    resultado_3 = models.CharField(max_length=255, blank=True)
    resultado_4 = models.CharField(max_length=255, blank=True)
    resultado_5 = models.CharField(max_length=255, blank=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Okr: {self.integrante}'
