from rest_framework import serializers, status
from rest_framework.exceptions import APIException
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from .models import Breed
from django.db.models.deletion import ProtectedError

class BreedReferenced(APIException):
    status_code = status.HTTP_424_FAILED_DEPENDENCY
    default_detail = "Can't delete referenced breed"


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ('uuid', 'name')


class BreedRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.get_queryset()
    serializer_class = BreedSerializer
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except ProtectedError:
            raise BreedReferenced()


class BreedCreateView(CreateAPIView):
    queryset = Breed.objects.get_queryset()
    serializer_class = BreedSerializer


class BreedListView(ListAPIView):
    queryset = Breed.objects.get_queryset()
    serializer_class = BreedSerializer
