from django.urls import path
from . import views

urlpatterns = [
    path('teacher-detail/<int:pk>/', views.TeacherDetail.as_view(), name='teacher'),
    path('teacher-list/', views.TeacherList.as_view(), name='teacher_list'),
    path('recruiter-detail/<int:pk>/', views.RecruiterDetail.as_view(), name='recruiter'),
    path('recruiter-list/', views.RecruiterList.as_view(), name='teacher_list'),
    path('recruiter-create/', views.RecruiterCreate.as_view(), name='add_recruiter'),
]