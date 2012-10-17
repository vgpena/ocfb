# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Photo.image' to match new field type.
        db.rename_column('gallery_photo', 'image', 'image_id')
        # Changing field 'Photo.image'
        db.alter_column('gallery_photo', 'image_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['daguerre.Image']))
        # Adding index on 'Photo', fields ['image']
        db.create_index('gallery_photo', ['image_id'])


    def backwards(self, orm):
        # Removing index on 'Photo', fields ['image']
        db.delete_index('gallery_photo', ['image_id'])


        # Renaming column for 'Photo.image' to match new field type.
        db.rename_column('gallery_photo', 'image_id', 'image')
        # Changing field 'Photo.image'
        db.alter_column('gallery_photo', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

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

    complete_apps = ['gallery']