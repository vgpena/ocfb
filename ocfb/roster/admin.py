from django.contrib import admin

from roster.models import Member




class MemberAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("last_name","first_name",)}
	
	
	
	
admin.site.register(Member, MemberAdmin)