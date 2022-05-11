from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class UserTeacher(models.Model):
    fullname = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.fullname

class UserStudent(models.Model):
    fullname = models.CharField(max_length=100)
    sclass = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.fullname