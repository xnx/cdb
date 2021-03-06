# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-03 13:45
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import sortedm2m.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('affiliation', models.CharField(max_length=500)),
                ('publication_doi', models.CharField(max_length=50)),
                ('general_comments', models.TextField(blank=True)),
                ('acknowledgements', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CDBRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('initial_configuration_filename', models.CharField(blank=True, max_length=100)),
                ('initial_configuration_comments', models.TextField(blank=True)),
                ('atomic_number', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(118)], verbose_name='PKA atomic number')),
                ('energy', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='PKA energy /eV')),
                ('recoil', models.BooleanField(default=True, verbose_name='PKA by recoil?')),
                ('electronic_stopping', models.BooleanField(default=False)),
                ('thermostat', models.BooleanField(default=False)),
                ('total_simulation_time', models.FloatField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total simulation time /ps')),
                ('initial_temperature', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('interatomic_potential_filename', models.CharField(max_length=100)),
                ('interatomic_potential_comment', models.TextField(blank=True)),
                ('code_name', models.CharField(max_length=100)),
                ('code_version', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'CDB record',
                'verbose_name_plural': 'CDB records',
            },
        ),
        migrations.CreateModel(
            name='DataColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('units', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LatticeParameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.FloatField(verbose_name='a /Å')),
                ('b', models.FloatField(verbose_name='b /Å')),
                ('c', models.FloatField(verbose_name='c /Å')),
                ('alpha', models.FloatField(verbose_name='α /deg')),
                ('beta', models.FloatField(verbose_name='β /deg')),
                ('gamma', models.FloatField(verbose_name='γ /deg')),
            ],
            options={
                'verbose_name_plural': 'Lattice parameters',
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chemical_formula', models.CharField(max_length=100)),
                ('structure', models.CharField(choices=[('fcc', 'face-centred cubic'), ('bcc', 'body-centred cubic'), ('hcp', 'hexagonal close packed'), ('dia', 'diamond'), ('amorphous', 'amorphous'), ('other', 'other')], max_length=100)),
                ('has_surface', models.BooleanField(default=False)),
                ('initially_perfect', models.BooleanField(default=True)),
                ('lattice_parameters', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cdbmeta.LatticeParameters')),
            ],
        ),
        migrations.AddField(
            model_name='cdbrecord',
            name='additional_columns',
            field=sortedm2m.fields.SortedManyToManyField(blank=True, help_text=None, to='cdbmeta.DataColumn'),
        ),
        migrations.AddField(
            model_name='cdbrecord',
            name='attribution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdbmeta.Attribution'),
        ),
        migrations.AddField(
            model_name='cdbrecord',
            name='material',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cdbmeta.Material'),
        ),
    ]
