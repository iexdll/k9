from django.test import TestCase, Client
from breeds.models import Breed

class BreedsModelsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        Breed.objects.create(name='Akita')

    def test_breed_creation(self):
        Breed.objects.create(name='Bulldog')
        self.assertEqual(Breed.objects.count(), 2)