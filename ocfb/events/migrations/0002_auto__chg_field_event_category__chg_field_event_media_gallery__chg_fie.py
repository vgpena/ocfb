# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Event.category'
        db.alter_column('events_event', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['events.Category'], null=True))

        # Changing field 'Event.media_gallery'
        db.alter_column('events_event', 'media_gallery_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Gallery'], null=True))

        # Changing field 'Event.preview_image'
        db.alter_column('events_event', 'preview_image_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gallery.Photo'], null=True))

    def backwards(self, orm):

        # Changing field 'Event.category'
        db.alter_column('events_event', 'category_id', self.gf('django.db.models.fields.related.ForeignKey')(default='lol', to=orm['events.Category']))

        # Changing field 'Event.media_gallery'
        db.alter_column('events_event', 'media_gallery_id', self.gf('django.db.models.fields.related.ForeignKey')(default='lol', to=orm['gallery.Gallery']))

        # Changing field 'Event.preview_image'
        db.alter_column('events_event', 'preview_image_id', self.gf('django.db.models.fields.related.ForeignKey')(default='lol', to=orm['gallery.Photo']))

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
        'events.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['events.Category']", 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'media_gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Gallery']", 'null': 'True', 'blank': 'True'}),
            'preview_image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Photo']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'gallery.photo': {
            'Meta': {'object_name': 'Photo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'credit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gallery.Gallery']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['daguerre.Image']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['events']