# Generated by Django 2.1 on 2018-08-20 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180820_0102'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovMensalistas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pagamento', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mensalista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Mensalista')),
            ],
        ),
    ]
