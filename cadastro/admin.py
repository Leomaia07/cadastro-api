from django.contrib import admin

# Register your models here.
from cadastro import models

@admin.register(models.cadastro)
class CadastroAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf','telefone','email','rua','bairro','numero')
    search_fields = ()
    list_filter = ()

