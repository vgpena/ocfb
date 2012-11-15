# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Gallery.title'
        db.add_column('gallery_gallery', 'title',
                      self.gf('django.db.models.fields.CharField')(default='hey', max_length=200),
                      keep_default=False)

        # Adding field 'Gallery.slug'
        db.add_column('gallery_gallery', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='hey', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Gallery.title'
        db.delete_column('gallery_gallery', 'title')

        # Deleting field 'Gallery.slug'
        db.delete_column('gallery_gallery', 'slug')


    models = {
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
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['gallery']