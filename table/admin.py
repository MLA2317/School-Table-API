from django.contrib import admin
from .models import Week, TableItem, Table, Time


class TableItemInline(admin.TabularInline):
    model = TableItem
    extra = 1


@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    inlines = [TableItemInline]
    list_display = ['id', 'title']


@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['id', 'time']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['id', 'shift', 'created_date']


