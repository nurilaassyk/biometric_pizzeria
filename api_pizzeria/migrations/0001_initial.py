# Generated by Django 4.2.5 on 2023-09-27 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PizzeriaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated date')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Deleted at')),
                ('name', models.CharField(blank=True, null=True, verbose_name='Name')),
                ('address', models.CharField(blank=True, null=True, verbose_name='Address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PizzaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(auto_now_add=True, verbose_name='Updated date')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Deleted at')),
                ('name', models.CharField(blank=True, null=True, verbose_name='Name')),
                ('cheese', models.CharField(blank=True, null=True, verbose_name='Types of cheese')),
                ('dough', models.CharField(blank=True, null=True, verbose_name='Dough thickness')),
                ('secret_ingredient', models.CharField(blank=True, null=True, verbose_name='Secret ingredient')),
                ('pizzeria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_pizzeria.pizzeriamodel', verbose_name='Pizzeria')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
