# Generated by Django 4.2.3 on 2023-08-01 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0002_remove_tableitem_shift_remove_tableitem_week_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weeks', to='table.week'),
        ),
    ]
