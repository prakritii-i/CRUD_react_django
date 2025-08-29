# tells django how to convert or JSON data to django model type
from rest_framework import serializers
from .models import book


# will be used whenever you want to convert json data kto python data
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'