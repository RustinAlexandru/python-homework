# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPostComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(max_length=100)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('author', models.CharField(default=b'Eau De Web', max_length=20)),
                ('post', models.ForeignKey(to='socialapp.UserPost')),
            ],
        ),
    ]
