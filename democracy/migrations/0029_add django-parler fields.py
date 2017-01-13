# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-08 11:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.utils.translation import ugettext_lazy as _


class Migration(migrations.Migration):

    dependencies = [
        ('democracy', '0028_n_unregistered_votes_editable_false'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPersonTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='democracy.ContactPerson')),
            ],
            options={
                'verbose_name': 'contact person Translation',
                'managed': True,
                'db_table': 'democracy_contactperson_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.AlterField(
            model_name='contactperson',
            name='title',
            field=models.CharField(verbose_name=_('title'), max_length=255, default='', null=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='HearingTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('borough', models.CharField(blank=True, default='', max_length=200, verbose_name='borough')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='democracy.Hearing')),
            ],
            options={
                'verbose_name': 'hearing Translation',
                'managed': True,
                'db_table': 'democracy_hearing_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.AlterField(
            model_name='hearing',
            name='title',
            field=models.CharField(verbose_name=_('title'), max_length=255, default='', null=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='LabelTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('label', models.CharField(default='', max_length=200, verbose_name='label')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='democracy.Label')),
            ],
            options={
                'verbose_name': 'label Translation',
                'managed': True,
                'db_table': 'democracy_label_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SectionImageTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(blank=True, default='', max_length=255, verbose_name='title')),
                ('caption', models.TextField(blank=True, default='', verbose_name='caption')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='democracy.SectionImage')),
            ],
            options={
                'verbose_name': 'section image Translation',
                'managed': True,
                'db_table': 'democracy_sectionimage_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.AlterField(
            model_name='sectionimage',
            name='title',
            field=models.CharField(verbose_name=_('title'), max_length=255, default='', null=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SectionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='title')),
                ('abstract', models.TextField(blank=True, verbose_name='abstract')),
                ('content', models.TextField(blank=True, verbose_name='content')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='democracy.Section')),
            ],
            options={
                'verbose_name': 'section Translation',
                'managed': True,
                'db_table': 'democracy_section_translation',
                'db_tablespace': '',
                'default_permissions': (),
            },
        ),
        migrations.AlterUniqueTogether(
            name='sectiontranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='sectionimagetranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='labeltranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='hearingtranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='contactpersontranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]