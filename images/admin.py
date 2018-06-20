from django.contrib import admin
from .models import Editor, Image, Category, Tag, Follow, Location, Profile, User, Comment



class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('category','tag', 'location' )



admin.site.register(Editor)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Follow)

# admin.site.register(Comment)




