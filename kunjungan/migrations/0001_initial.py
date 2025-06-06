# Generated by Django 5.1.7 on 2025-05-28 02:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kunjungan',
            fields=[
                ('id_kunjungan', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_hewan', models.CharField(max_length=50)),
                ('no_identitas_klien', models.UUIDField()),
                ('no_front_desk', models.UUIDField()),
                ('no_perawat_hewan', models.UUIDField()),
                ('no_dokter_hewan', models.UUIDField()),
                ('kode_vaksin', models.CharField(blank=True, max_length=6, null=True)),
                ('tipe_kunjungan', models.CharField(choices=[('Janji Temu', 'Janji Temu'), ('Walk-In', 'Walk-In'), ('Darurat', 'Darurat')], max_length=10)),
                ('timestamp_awal', models.DateTimeField()),
                ('timestamp_akhir', models.DateTimeField()),
                ('suhu', models.IntegerField(blank=True, null=True)),
                ('berat_badan', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('catatan', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'KUNJUNGAN',
                'unique_together': {('id_kunjungan', 'nama_hewan', 'no_identitas_klien', 'no_front_desk', 'no_perawat_hewan', 'no_dokter_hewan')},
            },
        ),
    ]
