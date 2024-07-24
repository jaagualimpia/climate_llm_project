from rest_framework import serializers

from api.models import QueryBasicModel

class QueryBasicModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryBasicModel
        fields = ['query', 'response']