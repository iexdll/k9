from rest_framework import serializers
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from dogs.models import Dog


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('uuid', 'name', 'breed')


class DogRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.get_queryset()
    serializer_class = DogSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


class DogCreateView(CreateAPIView):
    queryset = Dog.objects.get_queryset()
    serializer_class = DogSerializer
