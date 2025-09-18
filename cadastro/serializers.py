from rest_framework import serializers

from.models import cadastro
class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = cadastro
        fields = '__all__'


