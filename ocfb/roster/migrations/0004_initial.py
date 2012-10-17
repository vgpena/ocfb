# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Member'
        db.create_table('roster_member', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=40)),
            ('grad_year', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True, blank=True)),
            ('titles', self.gf('django.db.models.fields.CharField')(max_length=250, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('weapon', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('roster', ['Member'])


    def backwards(self, orm):
        # Deleting model 'Member'
        db.delete_table('roster_member')


    models = {
        'roster.member': {
            'Meta': {'object_name': 'Member'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'grad_year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'weapon': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['roster']