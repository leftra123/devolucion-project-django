# Generated by Django 4.1.3 on 2022-11-16 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("sistemaDeControlApp", "0003_alter_producto_fecha_de_creacion"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Producto",
            new_name="Devoluciones",
        ),
    ]