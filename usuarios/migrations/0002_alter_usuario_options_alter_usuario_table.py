# Generated by Django 4.2.1 on 2023-05-29 01:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'insira um nome para identificar no Django admin', 'verbose_name_plural': 'insira o nome acima no plural'},
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='nome que constará no banco de dados',
        ),
    ]
