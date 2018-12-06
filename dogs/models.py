import uuid
from django.db import models
from breeds.models import Breed

class Dog(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, default='')
    breed = models.ForeignKey(to=Breed, on_delete=models.PROTECT, null=True)
