# Generated by Django 5.0.2 on 2024-02-27 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuCB', '0004_season_isactive_barmenuitem_winemenuitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barmenuitem',
            options={'verbose_name': 'Барная карта', 'verbose_name_plural': 'Товары барной карты'},
        ),
        migrations.AlterModelOptions(
            name='mainmenuitem',
            options={'verbose_name': 'Основное меню', 'verbose_name_plural': 'Блюда основного меню'},
        ),
        migrations.AlterModelOptions(
            name='season',
            options={'verbose_name': 'Сезоны', 'verbose_name_plural': 'Сезоны'},
        ),
        migrations.AlterModelOptions(
            name='summermenuitem',
            options={'verbose_name': 'Летнее меню', 'verbose_name_plural': 'Блюда летнего меню'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Разделы', 'verbose_name_plural': 'Разделы'},
        ),
        migrations.AlterModelOptions(
            name='winemenuitem',
            options={'verbose_name': 'Винная карта', 'verbose_name_plural': 'Товары винной карты'},
        ),
        migrations.AlterModelOptions(
            name='wintermenuitem',
            options={'verbose_name': 'Зимнее меню', 'verbose_name_plural': 'Блюда зимнего меню'},
        ),
    ]
