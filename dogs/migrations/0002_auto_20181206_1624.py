# Generated by Django 2.1.4 on 2018-12-06 16:24

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('breeds', '0002_auto_20181206_1139'),
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dog',
            name='id',
        ),
        migrations.AddField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='breeds.Breed'),
        ),
        migrations.AddField(
            model_name='dog',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='dog',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
