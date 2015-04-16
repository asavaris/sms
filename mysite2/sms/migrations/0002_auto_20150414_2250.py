# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.RemoveField(
            model_name='leaderresponse',
            name='leaderform',
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.RemoveField(
            model_name='memberresponse',
            name='memberform',
        ),
        migrations.DeleteModel(
            name='LeaderForm',
        ),
        migrations.DeleteModel(
            name='LeaderResponse',
        ),
        migrations.DeleteModel(
            name='MemberForm',
        ),
        migrations.DeleteModel(
            name='MemberResponse',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='sms.Question'),
        ),
    ]
