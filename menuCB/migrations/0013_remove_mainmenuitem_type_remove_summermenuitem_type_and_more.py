# Generated by Django 5.0.2 on 2024-03-13 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menuCB', '0012_alter_type_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainmenuitem',
            name='type',
        ),
        migrations.RemoveField(
            model_name='summermenuitem',
            name='type',
        ),
        migrations.RemoveField(
            model_name='winemenuitem',
            name='type',
        ),
        migrations.RemoveField(
            model_name='wintermenuitem',
            name='type',
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название блюда')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img/%Y/%m/%d/', verbose_name='Изображение блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание блюда')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuCB.menu', verbose_name='Меню')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menuCB.type', verbose_name='Тип блюда')),
            ],
            options={
                'verbose_name': 'Блюдо основного  меню',
                'verbose_name_plural': 'Блюда основного меню',
            },
        ),
        migrations.DeleteModel(
            name='BarMenuItem',
        ),
        migrations.DeleteModel(
            name='MainMenuItem',
        ),
        migrations.DeleteModel(
            name='SummerMenuItem',
        ),
        migrations.DeleteModel(
            name='WineMenuItem',
        ),
        migrations.DeleteModel(
            name='WinterMenuItem',
        ),
    ]
