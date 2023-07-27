from django.contrib import admin
from .models import Student, Group


class StudentInline(admin.TabularInline):
    model = Student
    extra = 1


class GroupAdmin(admin.ModelAdmin):
    inlines = [StudentInline]
    list_display = ['id', 'title']


admin.site.register(Group, GroupAdmin)

