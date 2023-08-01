from django.db import models
from group.models import Group
from lesson.models import Lesson


class Week(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title


class TableItem(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    time = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.lesson} - {self.group}'


class Table(models.Model):
    Para = (
        ('1', '1-Para'),
        ('2', '2-Para'),
        ('3', '3-Para'),
    )
    shift = models.CharField(max_length=20, choices=Para)
    week = models.ForeignKey(Week, on_delete=models.CASCADE, related_name='weeks')
    table_id = models.ForeignKey(TableItem, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} - {self.shift} || {self.week} - {self.table_id}'

