# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=10)),
                ('lastName', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=100)),
                ('notes', models.TextField(default=b'', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='store',
            field=models.ForeignKey(related_name='client', to='store.Store'),
        ),
    ]
