from django.contrib import admin

from gallery.models import Gallery, Photo


class PhotoAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("gallery", "image", "caption")}
	list_display = ("slug", "caption", "gallery",)
	
class PhotoInline(admin.StackedInline):
	model = Photo
	prepopulated_fields = {"slug": ("gallery", "image", "caption")}
	
class GalleryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ("title",)
	
	inlines = [ PhotoInline, ]
	
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)