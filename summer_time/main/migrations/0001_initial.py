# Generated by Django 4.2.6 on 2023-10-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KidParent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('age', models.PositiveIntegerField(verbose_name='Age')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Kid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('surname', models.CharField(max_length=50, verbose_name='Surname')),
                ('age', models.PositiveIntegerField(verbose_name='Age')),
                ('parent', models.ManyToManyField(to='main.kidparent')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
