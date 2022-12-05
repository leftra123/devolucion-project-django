# Generated by Django 4.1.3 on 2022-12-04 17:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sistemaDeControlApp', '0025_alter_devolucion_cliente_alter_devolucion_producto_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='devolucion',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='producto',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tipo',
            field=models.CharField(choices=[('', 'SELECCIONE UNA OPCION'), ('Supermercado', 'SUPERMERCADO'), ('Minimarket', 'MINIMARKET'), ('Estacion de servicio', 'ESTACION DE SERVICIO'), ('Otro', 'OTRO')], default='Araucania', max_length=100, verbose_name='Tipo de cliente'),
        ),
        migrations.AlterField(
            model_name='devolucion',
            name='distribuidora',
            field=models.CharField(choices=[('', 'SELECCIONE UNA DISTRIBUIDORA'), ('Region de Arica y Parinacota', 'REGION DE ARICA Y PARINACOTA'), ('Region de Tarapaca', 'REGION DE TARAPACA'), ('Region de Antofagasta', 'REGION DE ANTOFAGASTA'), ('Region de Atacama', 'REGION DE ATACAMA'), ('Region de Coquimbo', 'REGION DE COQUIMBO'), ('Region de Valparaiso', 'REGION DE VALPARAISO'), ('Region Metropolitana', 'REGION METROPOLITANA'), ("Region del Libertador General Bernardo O'Higgins", "REGION DEL LIBERTADOR GENERAL BERNARDO O'HIGGINS"), ('Region del Maule', 'REGION DEL MAULE'), ('Region del ÑUBLE', 'REGION DEL ÑUBLE'), ('Region del Biobio', 'REGION DEL BIOBIO'), ('Region de la Araucania', 'REGION DE LA ARAUCANIA'), ('Region de Los Rios', 'REGION DE LOS RIOS'), ('Region de Los Lagos', 'REGION DE LOS LAGOS'), ('Region de Aysen del General Carlos Ibanez del Campo', 'REGION DE AYSEN DEL GENERAL CARLOS IBANEZ DEL CAMPO'), ('Region de Magallanes y de la Antartica Chilena', 'REGION DE MAGALLANES Y DE LA ANTARTICA CHILENA')], max_length=100, verbose_name='Distribuidora'),
        ),
    ]