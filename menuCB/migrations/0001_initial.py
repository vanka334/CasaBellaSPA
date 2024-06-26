# Generated by Django 5.0.2 on 2024-02-13 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Тип блюда')),
            ],
        ),
        migrations.CreateModel(
            name='SummerMenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание блюда')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuCB.type', verbose_name='Тип блюда')),
            ],
        ),
        migrations.CreateModel(
            name='SpringMenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание блюда')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuCB.type', verbose_name='Тип блюда')),
            ],
        ),
        migrations.CreateModel(
            name='MainMenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание блюда')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuCB.type', verbose_name='Тип блюда')),
            ],
        ),
        migrations.CreateModel(
            name='AutumnMenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание блюда')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuCB.type', verbose_name='Тип блюда')),
            ],
        ),
        migrations.CreateModel(
            name='WinterMenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание блюда')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuCB.type', verbose_name='Тип блюда')),
            ],
        ),
    ]
