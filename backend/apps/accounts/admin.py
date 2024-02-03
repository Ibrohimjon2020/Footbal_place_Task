from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .user_forms import CustomUserChangeForm, CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = (
        "phone_number",
        "first_name",
        "role",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "phone_number",
        "first_name",
        "role",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone_number",
                    "password",
                    "otp_code",
                )
            },
        ),
        (
            "Personal Info", 
            {
                "fields": ("first_name", "role"),
            },
        ),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name", 
                    "role",
                    "phone_number",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("phone_number",)
    ordering = ("phone_number",)
    readonly_fields = ("otp_code",)


admin.site.register(User, CustomUserAdmin)
