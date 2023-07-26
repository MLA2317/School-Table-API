from django.db import models
from account.models import Account


class Student(models.Model):
    student = models.ForeignKey(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.CharField(max_length=50)
    student_image = models.ImageField(upload_to='student_img/', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Group(models.Model):
    title = models.CharField(max_length=221)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


