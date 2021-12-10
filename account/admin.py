from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nickname',
        'username',
        'email',
        'last_login',
        'date_joined')
    exclude = ("date_joined","groups","first_name", "last_name","created_time", "last_modified_time")
admin.site.register(User, UserAdmin)