from django.db import models

# Create your models here.


from django.db import models


class cadastro(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True, blank=True, null=True)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)

    class Meta:
        abstract = True

        def __str__(self):
            return self.nome

        class Meta:
            db_table = 'grupo'