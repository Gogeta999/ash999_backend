from django.contrib import admin
from .models import Category, Post,Tag

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'index', 'notion_id')
    exclude = ('created_time', "last_modified_time")


class PostAdmin(admin.ModelAdmin):
    # summernote_fields = ('content')
    exclude = ('created_time', "last_modified_time")


class TagAdmin(admin.ModelAdmin):
    exclude = ('created_time', "last_modified_time")

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
