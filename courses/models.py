from django.db import models
from account.models import *
# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE)
    course = models.ForeignKey(Course, models.CASCADE)
    enrolled_at = models.DateTimeField()

    def __str__(self):
        return f'User {self.user} enrolled in {self.course} Course.'
