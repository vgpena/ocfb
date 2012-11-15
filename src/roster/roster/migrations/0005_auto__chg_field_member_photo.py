# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Member.photo' to match new field type.
        db.rename_column('roster_member', 'photo', 'photo_id')
        # Changing field 'Member.photo'
        db.alter_column('roster_member', 'photo_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['daguerre.Image'], null=True))
        # Adding index on 'Member', fields ['photo']
        db.create_index('roster_member', ['photo_id'])


    def backwards(self, orm):
        # Removing index on 'Member', fields ['photo']
        db.delete_index('roster_member', ['photo_id'])


        # User chose to not deal with backwards NULL issues for 'Member.photo'
        raise RuntimeError("Cannot reverse this migration. 'Member.photo' and its values cannot be restored.")

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
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'grad_year': ('django.db.models.fields.IntegerField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['daguerre.Image']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '40'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'weapon': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['roster']