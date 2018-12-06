import json
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


class DogAPITestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        akita_inu = Breed.objects.create(name='Akita-inu')
        golden_retriever_uuid = Breed.objects.create(name='Golden Retriever')
        cls.hachiko_uuid = Dog.objects.create(name='Hachi-ko', breed=akita_inu).uuid
        cls.dug_uuid = Dog.objects.create(name='Dug', breed=golden_retriever_uuid).uuid

    def test_post_dog(self):
        response = self.client.post('/dog/', data='{"name": "Rex"}', content_type="application/json")
        self.assertEqual(response.status_code, 201)
        created = json.loads(response.content)
        self.assertTrue(created)
        self.assertTrue(Dog.objects.filter(uuid=created['uuid']).exists())

    def test_get_dog(self):
        response = self.client.get('/dog/{0}/'.format(self.hachiko_uuid))
        self.assertEqual(response.status_code, 200)

    def test_update_dog(self):
        breed_uuid = Breed.objects.create(name='Akita-inu').uuid
        response = self.client.patch(
            '/dog/{0}/'.format(self.hachiko_uuid),
            '{{"breed": "{0}"}}'.format(breed_uuid),
            content_type="application/json")
        self.assertEqual(response.status_code, 200)
        updated = Dog.objects.get(uuid=self.hachiko_uuid)
        self.assertEqual(updated.breed.pk, breed_uuid)

    def test_delete_dog(self):
        response = self.client.delete('/dog/{0}/'.format(self.hachiko_uuid))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Dog.objects.filter(uuid=self.hachiko_uuid).exists())

    def test_get_all_dogs(self):
        response = self.client.get('/dogs/')
        self.assertEqual(response.status_code, 200)
        dogs_list = json.loads(response.content)
        self.assertEqual(len(dogs_list), 2)
        self.assertTrue(dogs_list[0])