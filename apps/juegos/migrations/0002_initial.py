# Generated by Django 4.2.1 on 2023-06-08 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('juegos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='telefonos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rams',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.tiporam'),
        ),
        migrations.AddField(
            model_name='rams',
            name='velocidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='juegos.ramsvelocidades'),
        ),
        migrations.AddField(
            model_name='historiales',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='graficas',
            name='gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='juegos.graficasgb'),
        ),
        migrations.AddField(
            model_name='graficas',
            name='velocidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='juegos.graficasvelocidades'),
        ),
        migrations.AddField(
            model_name='favoritos_urljuegos',
            name='favorito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.favoritos'),
        ),
        migrations.AddField(
            model_name='favoritos_urljuegos',
            name='urlJuego',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.urljuegos'),
        ),
        migrations.AddField(
            model_name='favoritos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dispositivos',
            name='grafica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.graficas'),
        ),
        migrations.AddField(
            model_name='dispositivos',
            name='procesador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.procesadores'),
        ),
        migrations.AddField(
            model_name='dispositivos',
            name='ram',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.rams'),
        ),
        migrations.AddField(
            model_name='dispositivos',
            name='sistemaOperativo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juegos.sistemasoperativos'),
        ),
        migrations.AddField(
            model_name='dispositivos',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]