from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Dweet, Profile

class ProfileInline(admin.StackedInline):
	model = Profile

class UserAdmin(admin.ModelAdmin):
	model = User
	fields = ["username"]
	inlines = [ProfileInline]

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Dweet)
# admin.site.register(Profile)