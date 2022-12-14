# Generated by Django 4.1.3 on 2022-12-04 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaDeControlApp', '0024_alter_devolucion_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devolucion',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sistemaDeControlApp.cliente'),
        ),
        migrations.AlterField(
            model_name='devolucion',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sistemaDeControlApp.producto'),
        ),
        migrations.AlterField(
            model_name='devolucion',
            name='vendedor',
            field=models.CharField(max_length=100, verbose_name='Vendedor'),
        ),
    ]
