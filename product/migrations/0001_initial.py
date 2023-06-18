# Generated by Django 4.2.2 on 2023-06-17 18:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.FloatField()),
                ('manufacturerdate', models.DateField()),
                ('rating', models.FloatField()),
                ('imageurl', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'products',
                'ordering': ['-createdAt'],
            },
        ),
    ]