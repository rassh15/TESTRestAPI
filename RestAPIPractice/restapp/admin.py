from django.contrib import admin
from restapp.models import UserStudent, UserTeacher

# Register your models here.
admin.site.register(UserTeacher)
admin.site.register(UserStudent)