# Generated by Django 4.2.3 on 2023-07-28 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_student_is_have_alter_student_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student',
        ),
    ]