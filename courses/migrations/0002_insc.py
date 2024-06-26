# Generated by Django 5.0.3 on 2024-03-27 22:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Insc',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('formation_id', models.UUIDField()),
                ('etudiant_id', models.IntegerField()),
                ('confirmed', models.BooleanField(default=False)),
            ],
        ),
    ]
