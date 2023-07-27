# Generated by Django 4.2.3 on 2023-07-27 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lesson_num',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.lessonroom'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='subject_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.subject'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teach_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson.teacher'),
        ),
    ]
