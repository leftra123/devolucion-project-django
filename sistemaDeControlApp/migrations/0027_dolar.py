# Generated by Django 4.1.3 on 2022-12-04 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaDeControlApp', '0026_devolucion_user_producto_user_alter_cliente_tipo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dolar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('valor', models.FloatField()),
            ],
        ),
    ]
