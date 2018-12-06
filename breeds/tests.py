from django.test import TestCase, Client
from breeds.models import Breed

class BreedsModelsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.akita_uuid = Breed.objects.create(name='Akita').uuid

    def test_breed_creation(self):
        bulldog = Breed.objects.create(name='Bulldog')
        saved_breed = Breed.objects.get(uuid=bulldog.uuid)
        self.assertEqual(saved_breed, bulldog)

    def test_breed_read(self):
        akita_breed = Breed.objects.get(uuid=self.akita_uuid)
        self.assertEqual(akita_breed.name, 'Akita')

    def test_breed_update(self):
        akita_breed = Breed.objects.get(uuid=self.akita_uuid)
        akita_breed.name = 'Akita-inu'
        akita_breed.save()
        updated_breed = Breed.objects.get(uuid=self.akita_uuid)
        self.assertEqual(updated_breed.name, 'Akita-inu')

    def test_breed_delete(self):
        Breed.objects.filter(uuid=self.akita_uuid).delete()
        self.assertEqual(Breed.objects.exists(), False)