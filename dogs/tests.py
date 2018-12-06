from django.test import TestCase
from breeds.models import Breed
from dogs.models import Dog

class DogsModelsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        akita_inu = Breed.objects.create(name='Akita-inu')
        cls.hachiko_uuid = Dog.objects.create(name='Hachi-ko', breed=akita_inu).uuid

    def test_dog_creation(self):
        rex = Dog.objects.create(name='Rex', breed=Breed.objects.create(name='Shepherd'))
        rex_from_db = Dog.objects.get(uuid=rex.uuid)
        self.assertEqual(rex_from_db, rex)

    def test_dog_read(self):
        hachiko = Dog.objects.get(uuid=self.hachiko_uuid)
        self.assertEqual(hachiko.name, 'Hachi-ko')

    def test_dog_update(self):
        hachiko = Dog.objects.get(uuid=self.hachiko_uuid)
        hachiko.name = "Hachi-ko - man's best friend"
        hachiko.save()
        hachiko_from_db = Dog.objects.get(uuid=self.hachiko_uuid)
        self.assertEqual(hachiko_from_db.name, "Hachi-ko - man's best friend")

    def test_dog_delete(self):
        Dog.objects.filter(uuid=self.hachiko_uuid).delete()
        self.assertFalse(Dog.objects.filter(uuid=self.hachiko_uuid).exists()) # ;_;
