from django.shortcuts import render
from ..models import Table, TableItem, Week, Time
from group.models import Group
from django.views.generic import ListView
from lesson.models import Lesson


# def index(request):
#     groups = Group.objects.all()
#     weeks = Week.objects.all()
#     # lesson = Lesson.objects.all()
#     table_item = TableItem.objects.filter(week__in=weeks)
#     group = Group.objects.filter(week__in=weeks)
#
#     tables = Table.objects.filter(table_id__in=table_item, table_id__group_id__in=group)
#     print(tables)
#
#     context = {
#         'groups': groups,
#         'weeks': weeks,
#         'tables':  tables,
#     }
#     return render(request, 'index.html', context)

def index(request):
    week = Week.objects.all()
    groups = Group.objects.all()
    table_items = TableItem.objects.all()
    tables = Table.objects.all()

    ctx = {
        'weeks': week,
        'groups': groups,
        'tables': tables,
        'table_items': table_items,
    }
    return render(request, 'index.html', ctx)

# def index(request):
#     groups = Group.objects.all()
#     weeks = Week.objects.all()
#     table_id = TableItem.objects.all()
#     tables = Table.objects.filter(table_id__in=table_id, table_id__group_id__in=groups)
#     print(tables)
#
#     context = {
#         'groups': groups,
#         'weeks': weeks,
#         'tables': tables,
#     }
#     return render(request, 'index.html', context)

# def index(request):
#     groups = Group.objects.all()
#     weeks = Week.objects.all()
#     context = {
#         'groups': groups,
#         'weeks': weeks,
#         'tables': {},
#     }
#
#     for group in groups:
#         group_tables = {}
#         for week in weeks:
#             week_tables = Table.objects.filter(week=week, table_id__group=group).order_by('created_date')
#             group_tables[week.id] = week_tables
#         context['tables'][group.id] = group_tables
#
#     return render(request, 'index.html', context)
