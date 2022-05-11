from dataclasses import field, fields
from email.policy import default
from rest_framework import serializers
from restapp.models import UserStudent,UserTeacher


class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())    
    class Meta:
        model = UserTeacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UserStudent
        fields = '__all__'