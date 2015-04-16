# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0005_auto_20150414_2256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberresponse',
            old_name='m_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='memberresponse',
            old_name='m_numMatches',
            new_name='numMatches',
        ),
        migrations.RenameField(
            model_name='memberresponse',
            old_name='m_prefs',
            new_name='prefs',
        ),
    ]
