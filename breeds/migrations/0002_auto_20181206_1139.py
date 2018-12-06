# Generated by Django 2.1.4 on 2018-12-06 11:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('breeds', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breed',
            name='id',
        ),
        migrations.AddField(
            model_name='breed',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='breed',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
