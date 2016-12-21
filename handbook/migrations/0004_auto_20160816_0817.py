# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import handbook.models.access
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0003_auto_20160315_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-name'], 'verbose_name': 'Name', 'verbose_name_plural': 'Names'},
        ),
        migrations.AlterModelOptions(
            name='organizerkey',
            options={'ordering': ['person'], 'verbose_name': 'Organizer Key', 'verbose_name_plural': 'Organizes Key'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='Message'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(verbose_name='Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='position',
            field=models.IntegerField(null=True, verbose_name='Position', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(unique=True, max_length=60, verbose_name='slug', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(unique=True, max_length=255, verbose_name='Title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='topic',
            field=models.ForeignKey(verbose_name='Topic', to='handbook.Topic'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizerkey',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizerkey',
            name='creator',
            field=models.ForeignKey(verbose_name='Creator', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizerkey',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='Exists'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizerkey',
            name='in_use',
            field=models.BooleanField(default=False, verbose_name='In Use'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizerkey',
            name='key',
            field=models.CharField(default=handbook.models.access.generate_key, max_length=100, verbose_name='Key'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='position',
            field=models.IntegerField(null=True, verbose_name='Position', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(unique=True, max_length=60, verbose_name='slug', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(unique=True, max_length=255, verbose_name='Title'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='version',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='version',
            name='version',
            field=models.IntegerField(default=1, verbose_name='Version'),
            preserve_default=True,
        ),
    ]
