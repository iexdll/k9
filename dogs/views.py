from rest_framework import serializers
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
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


class DogListView(ListAPIView):
    serializer_class = DogSerializer

    def get_queryset(self):
        queryset = Dog.objects.get_queryset()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name=name)
        return queryset