from rest_framework import serializers
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('uuid', 'name')


class BreedRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.get_queryset()
    serializer_class = BreedSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'


class BreedCreateView(CreateAPIView):
    queryset = Breed.objects.get_queryset()
    serializer_class = BreedSerializer