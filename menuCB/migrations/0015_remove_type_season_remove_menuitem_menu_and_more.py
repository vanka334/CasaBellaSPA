# Generated by Django 5.0.2 on 2024-04-22 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menuCB', '0014_menu_tags_menuitem_tags_type_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='season',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='type',
        ),
        migrations.RemoveField(
            model_name='type',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
