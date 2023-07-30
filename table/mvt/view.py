from django.shortcuts import render
from ..models import Table, TableItem


def index(request):
    table = Table.objects.all()
    table_item = TableItem.objects.all()
    ctx = {
        'tables': table,
        'table_items': table_item
    }
    return render(request, 'index.html', ctx)
