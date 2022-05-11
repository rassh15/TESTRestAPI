
from django.urls import path
from restapp import views
from restapp.models import UserTeacher
from restapp.models import UserStudent

urlpatterns = [
    path('api/teacher',views.TeacherAPIView.as_view()),
    path('api/student',views.StudentAPIView.as_view()),
    path('api/teacher/<int:pk>/', views.TeacherDetail.as_view()),
    path('api/student/<int:pk>/', views.StudentDetail.as_view()),
]
