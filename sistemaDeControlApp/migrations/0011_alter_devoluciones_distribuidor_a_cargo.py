# Generated by Django 4.1.3 on 2022-11-19 03:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("sistemaDeControlApp", "0010_remove_devoluciones_descripcion_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="devoluciones",
            name="distribuidor_a_cargo",
            field=models.CharField(
                default=django.utils.timezone.now,
                max_length=100,
                verbose_name="Distribuidor",
            ),
            preserve_default=False,
        ),
    ]