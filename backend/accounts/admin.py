from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    # Fields to display in the admin list view
    list_display = ('email', 'is_staff', 'is_superuser', 'is_active')
    
    # Fields to filter by
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    
    # Fields you can search for
    search_fields = ('email',)
    
    # Fields displayed on the user detail page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions')}),
    )
    
    # Fields when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active'),
        }),
    )
    
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

# Make this model visible in the admin panel
admin.site.register(User, UserAdmin)
admin.site.site_header = "CBoard Admin"
admin.site.index_title = "User Management"
admin.site.site_title = "CBoard Admin"
