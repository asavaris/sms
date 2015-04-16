# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_auto_20150414_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberResponse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('m_name', models.CharField(max_length=100)),
                ('numMatches', models.IntegerField(default=0)),
                ('which_login', models.ForeignKey(to='sms.LoginInfo')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
    ]
