from django.contrib import admin
from .models import Week, TableItem, Table


@admin.register(Week)
class WeekAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(TableItem)
class TableItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'group', 'lesson', 'time']
    search_fields = ['lesson']


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['id', 'shift', 'week', 'table_id', 'created_date']


