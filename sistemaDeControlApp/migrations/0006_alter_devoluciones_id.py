# Generated by Django 4.1.3 on 2022-11-19 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sistemaDeControlApp", "0005_alter_devoluciones_descripcion_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="devoluciones",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
