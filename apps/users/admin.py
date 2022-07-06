from django.contrib import admin
from apps.users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'name',
        'last_name',
        'is_active'
    )
admin.site.register(User,UserAdmin)
