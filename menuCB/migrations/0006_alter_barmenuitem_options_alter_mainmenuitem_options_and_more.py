# Generated by Django 5.0.2 on 2024-02-27 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuCB', '0005_alter_barmenuitem_options_alter_mainmenuitem_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barmenuitem',
            options={'verbose_name': 'Товар Барной карта', 'verbose_name_plural': 'Товары барной карты'},
        ),
        migrations.AlterModelOptions(
            name='mainmenuitem',
            options={'verbose_name': 'Блюдо Основного  меню', 'verbose_name_plural': 'Блюда основного меню'},
        ),
        migrations.AlterModelOptions(
            name='season',
            options={'verbose_name': 'Сезон', 'verbose_name_plural': 'Сезоны'},
        ),
        migrations.AlterModelOptions(
            name='summermenuitem',
            options={'verbose_name': 'Блюдо Летнего меню', 'verbose_name_plural': 'Блюда летнего меню'},
        ),
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
        migrations.AlterModelOptions(
            name='winemenuitem',
            options={'verbose_name': 'Товар Винной карта', 'verbose_name_plural': 'Товары винной карты'},
        ),
        migrations.AlterModelOptions(
            name='wintermenuitem',
            options={'verbose_name': 'Блюдо Зимнего меню', 'verbose_name_plural': 'Блюда зимнего меню'},
        ),
    ]
