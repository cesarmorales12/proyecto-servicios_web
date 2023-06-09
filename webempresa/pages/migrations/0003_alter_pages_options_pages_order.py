# Generated by Django 4.1.7 on 2023-04-11 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_url_pages_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pages',
            options={'ordering': ['order', 'title'], 'verbose_name': 'página', 'verbose_name_plural': 'páginas'},
        ),
        migrations.AddField(
            model_name='pages',
            name='order',
            field=models.SmallIntegerField(default=0, verbose_name='Orden'),
        ),
    ]
