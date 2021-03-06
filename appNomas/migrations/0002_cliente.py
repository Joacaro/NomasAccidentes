# Generated by Django 3.1.1 on 2021-07-01 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appNomas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10, unique=True)),
                ('direccion', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
                ('last_login', models.DateTimeField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
