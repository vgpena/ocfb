# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Member.gender'
        db.alter_column('roster_member', 'gender', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Member.weapon'
        db.alter_column('roster_member', 'weapon', self.gf('django.db.models.fields.CharField')(max_length=10))

    def backwards(self, orm):

        # Changing field 'Member.gender'
        db.alter_column('roster_member', 'gender', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Member.weapon'
        db.alter_column('roster_member', 'weapon', self.gf('django.db.models.fields.CharField')(max_length=1))

    models = {
        'daguerre.image': {
            'Meta': {'object_name': 'Image'},
            'height': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'width': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        'roster.member': {
            'Meta': {'object_name': 'Member'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'grad_year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['daguerre.Image']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'weapon': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['roster']