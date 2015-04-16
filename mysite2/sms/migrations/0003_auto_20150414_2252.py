# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20150414_2250'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('survey_id', models.CharField(max_length=15)),
                ('user_password', models.CharField(max_length=15)),
                ('member_password', models.CharField(max_length=15)),
                ('leader_password', models.CharField(max_length=15)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='sms.LoginInfo'),
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
