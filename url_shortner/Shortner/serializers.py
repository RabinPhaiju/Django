from rest_framework import serializers
from . models import URLData

class URLDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = URLData
        field = '__all__'