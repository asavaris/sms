# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0004_auto_20150414_2253'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberresponse',
            old_name='numMatches',
            new_name='m_numMatches',
        ),
        migrations.AddField(
            model_name='memberresponse',
            name='m_prefs',
            field=models.CharField(default=b'null', max_length=300),
        ),
        migrations.AlterField(
            model_name='memberresponse',
            name='m_name',
            field=models.CharField(default=b'null', max_length=100),
        ),
    ]
