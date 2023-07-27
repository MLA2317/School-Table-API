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

    def __str__(self):
        return f'{self.room_num} - {self.room_type}'


class Teacher(models.Model):
    teacher = models.ForeignKey(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    subject_taught = models.CharField(max_length=50)
    Level = (
        ('Small degree', '1'),
        ('Middle degree', '2'),
        ('Big degree', '3')
    )
    level = models.CharField(choices=Level, max_length=40)
    teacher_img = models.ImageField(upload_to='teacher_img/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Lesson(models.Model):
    lesson_num = models.ForeignKey(LessonRoom, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teach_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    duration = models.IntegerField()
    time = models.CharField(max_length=10)

    def __str__(self):
        return f"Xona: {self.lesson_num} || Mavzu: {self.subject_id} -> {self.duration}"


