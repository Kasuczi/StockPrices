# Generated by Django 3.0.8 on 2020-07-04 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Index',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PriceAlert',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Currency')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Index')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=255)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Currency')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Index')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Source')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
