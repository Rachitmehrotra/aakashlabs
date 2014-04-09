# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Coordinator'
        db.create_table(u'ac_coordinator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('contact', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'ac', ['Coordinator'])

        # Adding model 'AakashCentre'
        db.create_table(u'ac_aakashcentre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ac_id', self.gf('django.db.models.fields.IntegerField')(unique=True, max_length=6)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=7)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('coordinator', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ac.Coordinator'], unique=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ac', ['AakashCentre'])

        # Adding model 'Project'
        db.create_table(u'ac_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('ac', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ac.AakashCentre'])),
            ('summary', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('src_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('doc_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('doc_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('apk', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('additional_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('download_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date_uploaded', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
            ('rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('approve', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ac', ['Project'])

        # Adding model 'TeamMember'
        db.create_table(u'ac_teammember', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('member_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('member_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('member_project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ac.Project'])),
        ))
        db.send_create_signal(u'ac', ['TeamMember'])

        # Adding model 'Mentor'
        db.create_table(u'ac_mentor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mentor_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('mentor_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('mentor_project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ac.Project'])),
        ))
        db.send_create_signal(u'ac', ['Mentor'])

        # Adding model 'Contact'
        db.create_table(u'ac_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('message', self.gf('django.db.models.fields.TextField')(max_length=500)),
        ))
        db.send_create_signal(u'ac', ['Contact'])

        # Adding model 'Faq'
        db.create_table(u'ac_faq', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('answer', self.gf('django.db.models.fields.TextField')(max_length=1000)),
        ))
        db.send_create_signal(u'ac', ['Faq'])

        # Adding model 'Pub'
        db.create_table(u'ac_pub', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(unique=True, max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=500, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('attachment', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'ac', ['Pub'])


    def backwards(self, orm):
        # Deleting model 'Coordinator'
        db.delete_table(u'ac_coordinator')

        # Deleting model 'AakashCentre'
        db.delete_table(u'ac_aakashcentre')

        # Deleting model 'Project'
        db.delete_table(u'ac_project')

        # Deleting model 'TeamMember'
        db.delete_table(u'ac_teammember')

        # Deleting model 'Mentor'
        db.delete_table(u'ac_mentor')

        # Deleting model 'Contact'
        db.delete_table(u'ac_contact')

        # Deleting model 'Faq'
        db.delete_table(u'ac_faq')

        # Deleting model 'Pub'
        db.delete_table(u'ac_pub')


    models = {
        u'ac.aakashcentre': {
            'Meta': {'object_name': 'AakashCentre'},
            'ac_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'max_length': '6'}),
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'coordinator': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ac.Coordinator']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '7'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'ac.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'ac.coordinator': {
            'Meta': {'object_name': 'Coordinator'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
        u'ac.faq': {
            'Meta': {'object_name': 'Faq'},
            'answer': ('django.db.models.fields.TextField', [], {'max_length': '1000'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'max_length': '500'})
        },
        u'ac.mentor': {
            'Meta': {'object_name': 'Mentor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mentor_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'mentor_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'mentor_project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ac.Project']"})
        },
        u'ac.project': {
            'Meta': {'object_name': 'Project'},
            'ac': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ac.AakashCentre']"}),
            'additional_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'apk': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'approve': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_uploaded': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'doc_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'doc_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'download_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'src_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'max_length': '500'})
        },
        u'ac.pub': {
            'Meta': {'object_name': 'Pub'},
            'attachment': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'ac.teammember': {
            'Meta': {'object_name': 'TeamMember'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'member_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'member_project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ac.Project']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['ac']