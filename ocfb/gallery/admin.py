from django.contrib import admin

from gallery.models import Gallery, Photo

	
class GalleryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	
	
class PhotoAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("caption","image",)}


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)