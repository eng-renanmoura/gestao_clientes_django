# Generated by Django 2.0.1 on 2018-08-29 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0004_auto_20180829_1404'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venda',
            options={'permissions': (('setar_nfe', 'Usuario pode alterar parametro NFe'), ('ver_dashboard', 'Ver dashboard'), ('permissao3', 'Permissao 3'))},
        ),
    ]