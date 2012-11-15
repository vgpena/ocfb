from django.contrib import admin

from roster.models import Member


class MemberAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("last_name","first_name",)}
	list_display = ("last_name", "first_name", "weapon",)
	radio_fields = {"gender": admin.HORIZONTAL, "weapon": admin.HORIZONTAL}


admin.site.register(Member, MemberAdmin)