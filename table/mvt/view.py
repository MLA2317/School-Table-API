from django.shortcuts import render
from ..models import Table, TableItem, Week
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
    groups = Group.objects.all()
    weeks = Week.objects.all()
    table_id = TableItem.objects.all()
    print(table_id)
    # tables = Table.objects.filter(week__in=weeks)
    # table_items = TableItem.objects.filter(id__in=[table.table_id.id for table in tables])
    tables = Table.objects.filter(week__in=weeks, table_id__in=table_id, table_id__groups__in=groups)

    context = {
        'groups': groups,
        'weeks': weeks,
        'tables': tables,
        # 'table_items': table_items,
        # 'filtered_groups': filtered_groups,
    }
    return render(request, 'index.html', context)

# def index(request):
#     groups = Group.objects.all()
#     weeks = Week.objects.all()
#
#     group_id = request.GET.get('group_id')
#     week_id = request.GET.get('week_id')
#     if group_id and week_id:
#         tables = Table.objects.filter(week_id=week_id, group_id=group_id)
#     else:
#         tables = Table.objects.all()
#
#     # Create an empty dict to hold your rows
#     table_rows = {}
#
#     for table in tables:
#         # Check if the row is not already in the dict
#         if table.row not in table_rows:
#             # If not, add an empty list to represent the row
#             table_rows[table.row] = []
#
#         # Append the table to its appropriate row
#         table_rows[table.row].append(table)
#
#     # Convert the dict to a list of lists to make it easier to work with in your template
#     table_matrix = [table_rows[key] for key in sorted(table_rows.keys())]
#
#     context = {
#         'groups': groups,
#         'weeks': weeks,
#         'tables': table_matrix,  # Use the table_matrix instead of tables
#     }
#
#     return render(request, 'base.html', context)
