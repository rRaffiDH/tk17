# Generated by Django 5.2.1 on 2025-05-23 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaksin',
            fields=[
                ('kode', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nama', models.CharField(max_length=50)),
                ('harga', models.IntegerField()),
                ('stok', models.IntegerField()),
            ],
            options={
                'db_table': 'VAKSIN',
            },
        ),
    ]
