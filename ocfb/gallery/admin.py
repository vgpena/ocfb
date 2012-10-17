from django.contrib import admin

from gallery.models import Gallery, Photo

	
class GalleryAdmin(admin.ModelAdmin):
	prepopulated_fields = {"slug": ("title",)}
	list_display = ("title",)
	
class PhotoAdmin(admin.ModelAdmin):
	list_display = ("image", "caption", "gallery",)


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Photo, PhotoAdmin)