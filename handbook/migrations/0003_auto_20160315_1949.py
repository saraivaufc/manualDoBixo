# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import handbook.models.access
import django.utils.timezone
from django.conf import settings
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('handbook', '0002_remove_person_exists'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-name'], 'verbose_name': 'Nome', 'verbose_name_plural': 'Nomes'},
        ),
        migrations.AlterModelOptions(
            name='organizerkey',
            options={'ordering': ['person'], 'verbose_name': 'Chave do Organizador', 'verbose_name_plural': 'Chaves dos Organizadores'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='Mensagem'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(verbose_name='Descri\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(default=None, upload_to=b'documents/%Y/%m/%d', verbose_name='Imagem'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='position',
            field=models.IntegerField(null=True, verbose_name='Posi\xe7\xe3o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(unique=True, max_length=60, verbose_name='Slug', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(unique=True, max_length=255, verbose_name='T\xedtulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='item',
            name='topic',
            field=models.ForeignKey(verbose_name='T\xf3pico', to='handbook.Topic'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizerkey',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizerkey',
            name='creator',
            field=models.ForeignKey(verbose_name='Criador', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizerkey',
            name='exists',
            field=models.BooleanField(default=True, verbose_name='Existe'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizerkey',
            name='in_use',
            field=models.BooleanField(default=False, verbose_name='Em uso'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='organizerkey',
            name='key',
            field=models.CharField(default=handbook.models.access.generate_key, max_length=100, verbose_name='Chave'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='creation',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Cria\xe7\xe3o'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='position',
            field=models.IntegerField(null=True, verbose_name='Posi\xe7\xe3o', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='slug',
            field=models.SlugField(unique=True, max_length=60, verbose_name='Slug', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='topic',
            name='title',
            field=models.CharField(unique=True, max_length=255, verbose_name='T\xedtulo'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='version',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='Nome'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='version',
            name='version',
            field=models.IntegerField(default=1, verbose_name='Vers\xe3o'),
            preserve_default=True,
        ),
    ]
