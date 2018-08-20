# Generated by Django 2.1 on 2018-08-20 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mensalista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MovRotativo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.DateTimeField()),
                ('checkout', models.DateTimeField(blank=True, null=True)),
                ('pago', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Parametro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=5)),
                ('valor_mes', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=200)),
                ('telefone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('placa', models.CharField(max_length=7)),
                ('cor', models.CharField(max_length=15)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Marca')),
                ('proprietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='movrotativo',
            name='valor_hora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Parametro'),
        ),
        migrations.AddField(
            model_name='movrotativo',
            name='veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo'),
        ),
        migrations.AddField(
            model_name='mensalista',
            name='valor_mes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Parametro'),
        ),
        migrations.AddField(
            model_name='mensalista',
            name='veiculo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Veiculo'),
        ),
    ]
