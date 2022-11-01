from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from authentication.models import User


class MyUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("role", "balance")}),)


# Register your models here.
admin.site.register(User, MyUserAdmin)
