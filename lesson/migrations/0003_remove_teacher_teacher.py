# Generated by Django 4.2.3 on 2023-07-28 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_alter_lesson_lesson_num_alter_lesson_subject_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='teacher',
        ),
    ]