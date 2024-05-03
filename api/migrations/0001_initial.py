# Generated by Django 5.0.2 on 2024-04-22 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='Меню')),
                ('isActive', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Тип блюда')),
                ('queue_view', models.IntegerField(default=0, verbose_name='Очередь показа на странице')),
                ('season', models.ForeignKey(max_length=2, on_delete=django.db.models.deletion.CASCADE, to='api.menu', verbose_name='Сезон')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название блюда')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d/', verbose_name='Изображение блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание блюда')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.menu', verbose_name='Меню')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.type', verbose_name='Тип блюда')),
            ],
            options={
                'verbose_name': 'Блюдо  меню',
                'verbose_name_plural': 'Блюда  меню',
            },
        ),
    ]
