# Generated by Django 5.0.4 on 2024-05-08 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('areas', '0001_initial'),
        ('tipositio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ambientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ambientes', models.CharField(max_length=200)),
                ('img', models.ImageField(null=True, upload_to='ambientes.Ambientes.img')),
                ('registro', models.DateTimeField(auto_now_add=True)),
                ('fk_area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='areas.area')),
                ('fk_tipo_sitio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tipositio.tipo_sitio')),
            ],
        ),
    ]
