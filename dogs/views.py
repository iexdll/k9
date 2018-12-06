from rest_framework import serializers
from rest_framework.generics import CreateAPIView
from dogs.models import Dog


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('uuid', 'name', 'breed')


class DogCreateView(CreateAPIView):
    queryset = Dog.objects.get_queryset()
    serializer_class = DogSerializer
