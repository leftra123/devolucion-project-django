# Generated by Django 4.1.3 on 2022-11-19 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "sistemaDeControlApp",
            "0012_alter_devoluciones_distribuidor_a_cargo_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="devoluciones",
            name="cantidad_devuelta",
            field=models.IntegerField(verbose_name="Cantidad"),
        ),
    ]
