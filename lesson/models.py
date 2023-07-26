from django.db import models
from account.models import Account


class Subject(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class LessonRoom(models.Model):
    Type = (
        ('1', 'Small'),
        ('2', 'Middle'),
        ('3', 'Big')
    )
    room_num = models.IntegerField(default=0)
    room_type = models.CharField(choices=Type, max_length=30)
    capacity = models.IntegerField(default=0)

    def __int__(self):
        return self.room_num


class Teacher(models.Model):
    teacher = models.ForeignKey(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject_taught = models.CharField(max_length=50)
    Level = (
        ('1', 'Small degree'),
        ('2', 'Middle degree'),
        ('3', 'Big degree')
    )
    level = models.CharField(choices=Level, max_length=40)
    teacher_img = models.ImageField(upload_to='teacher_img/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Lesson(models.Model):
    lesson_num_id = models.ForeignKey(LessonRoom, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teach_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    duration = models.IntegerField()
    time = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.lesson_num_id} - {self.duration}'


