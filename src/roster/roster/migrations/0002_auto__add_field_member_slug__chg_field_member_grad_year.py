# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Member.slug'
        db.add_column('roster_member', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='penaviolet', max_length=40),
                      keep_default=False)


        # Changing field 'Member.grad_year'
        db.alter_column('roster_member', 'grad_year', self.gf('django.db.models.fields.IntegerField')(max_length=4, null=True))

    def backwards(self, orm):
        # Deleting field 'Member.slug'
        db.delete_column('roster_member', 'slug')


        # User chose to not deal with backwards NULL issues for 'Member.grad_year'
        raise RuntimeError("Cannot reverse this migration. 'Member.grad_year' and its values cannot be restored.")

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