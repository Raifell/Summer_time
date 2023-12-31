# Generated by Django 4.2.6 on 2023-10-25 21:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_kid_parent_kid_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icecream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='kid',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='kidparent',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='kid',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.kidparent', verbose_name='Parent'),
        ),
        migrations.CreateModel(
            name='IcecreamShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('icecream', models.ManyToManyField(to='main.icecream')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
