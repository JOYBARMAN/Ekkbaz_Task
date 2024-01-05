from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Business


# Business model admin site
@admin.register(Business)
class BusinessAdmin(admin.ModelAdmin):
    list_display = (
        "user_name",
        "business_name",
        "latitude",
        "longitude",
    )
    search_fields = ("business_name",)

    def user_name(self, obj):
        return obj.user.username

    user_name.short_description = "Username"  # Set a custom column header
