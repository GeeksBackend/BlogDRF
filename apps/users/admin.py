from django.contrib import admin

from apps.users.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('username', 'first_name', 'last_name', 'email')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_per_page = 20

admin.site.register(User, UserAdmin)