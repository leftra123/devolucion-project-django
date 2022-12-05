# Generated by Django 4.1.3 on 2022-12-04 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaDeControlApp', '0023_cliente_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devolucion',
            name='cliente',
            field=models.ForeignKey(choices=[('Supermercado', 'SUPERMERCADO'), ('Minimarket', 'MINIMARKET'), ('Estacion de servicio', 'ESTACION DE SERVICIO'), ('Otro', 'OTRO')], on_delete=django.db.models.deletion.PROTECT, to='sistemaDeControlApp.cliente', verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='devolucion',
            name='distribuidora',
            field=models.CharField(choices=[('Region de Arica y Parinacota', 'REGION DE ARICA Y PARINACOTA'), ('Region de Tarapaca', 'REGION DE TARAPACA'), ('Region de Antofagasta', 'REGION DE ANTOFAGASTA'), ('Region de Atacama', 'REGION DE ATACAMA'), ('Region de Coquimbo', 'REGION DE COQUIMBO'), ('Region de Valparaiso', 'REGION DE VALPARAISO'), ('Region Metropolitana', 'REGION METROPOLITANA'), ("Region del Libertador General Bernardo O'Higgins", "REGION DEL LIBERTADOR GENERAL BERNARDO O'HIGGINS"), ('Region del Maule', 'REGION DEL MAULE'), ('Region del ÑUBLE', 'REGION DEL ÑUBLE'), ('Region del Biobio', 'REGION DEL BIOBIO'), ('Region de la Araucania', 'REGION DE LA ARAUCANIA'), ('Region de Los Rios', 'REGION DE LOS RIOS'), ('Region de Los Lagos', 'REGION DE LOS LAGOS'), ('Region de Aysen del General Carlos Ibanez del Campo', 'REGION DE AYSEN DEL GENERAL CARLOS IBANEZ DEL CAMPO'), ('Region de Magallanes y de la Antartica Chilena', 'REGION DE MAGALLANES Y DE LA ANTARTICA CHILENA')], max_length=100, verbose_name='Distribuidora'),
        ),
        migrations.AlterField(
            model_name='devolucion',
            name='producto',
            field=models.ForeignKey(choices=[('consumo', 'CONSUMO'), ('industria', 'INDUSTRIA'), ('panaderia', 'PANADERIA')], on_delete=django.db.models.deletion.PROTECT, to='sistemaDeControlApp.producto', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='devolucion',
            name='vendedor',
            field=models.CharField(choices=[('Juan', 'JUAN'), ('Pedro', 'PEDRO'), ('Maria', 'MARIA'), ('Jose', 'JOSE'), ('Luis', 'LUIS'), ('Rosa', 'ROSA'), ('Carlos', 'CARLOS'), ('Miguel', 'MIGUEL')], max_length=100, verbose_name='Vendedor'),
        ),
    ]