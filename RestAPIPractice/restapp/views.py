from multiprocessing import context
from urllib import request
from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from restapp.permissions import IsOwner
from restapp import serializers
from restapp.models import UserStudent,UserTeacher
from restapp.serializers import TeacherSerializer, StudentSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class TeacherAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = TeacherSerializer


    def get(self, request, format=None):
            
        data = UserTeacher.objects.filter(user=request.user)

        serializer = self.serializer_class(data, many=True)
        serialized_data = serializer.data  
        
        return Response(serialized_data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            serialized_data = serializer.data
            return Response(serialized_data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class StudentAPIView(APIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request, format=None):

        data = UserStudent.objects.filter(user=request.user)
        serializer = self.serializer_class(data, many=True)
        serialized_data = serializer.data
        return Response(serialized_data)

    def post(self, request, format=None):

        serializer = self.serializer_class(data = request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            print(request.data)
            serialized_data = serializer.data
            return Response(serialized_data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk):
        try:
            obj = UserStudent.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except UserStudent.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status = status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        studentdata = self.get_object(pk)
        serializer = self.serializer_class(studentdata, data=request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.Http_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        studentdata = self.get_object(pk)
        studentdata.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class TeacherDetail(APIView):
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_object(self, pk):
        try:
            obj = UserStudent.objects.get(pk=pk)
            self.check_object_permissions(self.request, obj)
            return obj
        except UserTeacher.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        serializer = self.serializer_class(self.get_object(pk))
        serialized_data = serializer.data
        return Response(serialized_data, status = status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        teacherdata = self.get_object(pk)
        serializer = self.serializer_class(teacherdata, data=request.data, context = {'request': request})
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.Http_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        teacherdata = self.get_object(pk)
        teacherdata.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)



