import json
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
        self.assertFalse(Breed.objects.exists())


class BreedAPITestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.akita_uuid = Breed.objects.create(name='Akita').uuid
        cls.bulldog_uuid = Breed.objects.create(name='Bulldog').uuid

    def setUp(self):
        self.client = Client()

    def test_post_breed(self):
        response = self.client.post('/breed/', data="{name: 'Poodle'}")
        self.assertEqual(response, 200)
        created = json.loads(response.body)
        self.assertTrue(created)
        self.assertTrue(Breed.objects.filter(uuid=created['uuid']).exists())

    def test_get_breed(self):
        response = self.client.get('/breed/%s/'.format(self.akita_uuid))
        self.assertEqual(response, 200)

    def test_update_breed(self):
        response = self.client.patch('/breed/%s/'.format(self.akita_uuid), "{name: 'Akita-inu'}")
        self.assertEqual(response.status_code, 200)
        updated = Breed.objects.get(uuid=self.akita_uuid)
        self.assertEqual(updated.name, 'Akita-inu')

    def test_delete_breed(self):
        response = self.client.delete('/breed/%s/'.format(self.akita_uuid))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Breed.objects.find(uuid=self.akita_uuid).exists())
