from django.contrib import admin
from .models import Photo, PhotoCategory

class PhotoAdmin(admin.ModelAdmin):
    pass
admin.site.register(Photo,PhotoAdmin)

class PhotoCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(PhotoCategory,PhotoCategoryAdmin)

