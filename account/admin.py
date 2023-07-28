from django.contrib import admin
from .models import OwnerModel,UserModel
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "first_name", 'roles')
    list_filter = ("username", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", 'roles'
            )
        }
         ),

    )
    search_fields = ("username",)
    ordering = ("username",)

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(UserModel)
admin.site.register(OwnerModel)
