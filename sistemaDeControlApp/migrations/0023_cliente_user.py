# Generated by Django 4.1.3 on 2022-12-03 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sistemaDeControlApp', '0022_alter_devolucion_monto_devolucion_usd'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
