# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0006_auto_20150414_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'null', max_length=100)),
                ('numMatches', models.IntegerField(default=0)),
                ('prefs', models.CharField(default=b'null', max_length=300)),
                ('which_login', models.ForeignKey(to='sms.LoginInfo')),
            ],
        ),
        migrations.AddField(
            model_name='memberresponse',
            name='conflicts',
            field=models.CharField(default=b'null', max_length=300),
        ),
    ]
