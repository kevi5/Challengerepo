from rest_framework import serializers
from .models import Books, Members, Circulation
class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class Memberserializer(serializers.ModelSerializer):    
    class Meta:
        model = Members
        fields = '__all__'

class Circulationserializer(serializers.ModelSerializer):
    class Meta:
        model = Circulation
        fields = '__all__'

