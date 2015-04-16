# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0007_auto_20150414_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logininfo',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='logininfo',
            name='question_text',
        ),
    ]
