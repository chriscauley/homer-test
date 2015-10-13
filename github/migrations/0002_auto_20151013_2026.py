# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='repository',
            unique_together=set([('username', 'reponame')]),
        ),
    ]