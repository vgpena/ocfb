from django.contrib import admin

from roster.models import Member
from gallery.models import Gallery, Photo




class MemberAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("last_name","first_name",)}
	
	
	

admin.site.register(Member, MemberAdmin)
admin.site.register(Gallery)
admin.site.register(Photo)