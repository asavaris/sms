# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('survey_id', models.CharField(max_length=200)),
                ('l_name', models.CharField(max_length=20)),
                ('prefs', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('l_name', models.CharField(max_length=20)),
                ('numMatches', models.IntegerField(default=0)),
                ('prefs', models.CharField(max_length=15)),
                ('leaderform', models.ForeignKey(to='sms.LeaderForm')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('survey_id', models.CharField(max_length=200)),
                ('Userpassword', models.CharField(max_length=15)),
                ('Memberpassword', models.CharField(max_length=15)),
                ('Leaderpassword', models.CharField(max_length=15)),
                ('datePublished', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='MemberForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('survey_id', models.CharField(max_length=200)),
                ('l_name', models.CharField(max_length=20)),
                ('prefs', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='MemberResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('m_name', models.CharField(max_length=20)),
                ('numMatches', models.IntegerField(default=0)),
                ('prefs', models.CharField(max_length=15)),
                ('conflicts', models.CharField(max_length=15)),
                ('memberform', models.ForeignKey(to='sms.MemberForm')),
            ],
        ),
    ]
