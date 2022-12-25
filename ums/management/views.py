from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import TeacherSerializer, RecruiterSerializer
from .models import Teacher, Recruiter

# Create your views here.

class TeacherDetail(RetrieveAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()

class TeacherList(ListAPIView):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    
class RecruiterCreate(CreateAPIView):
    serializer_class = RecruiterSerializer
    queryset = Recruiter.objects.all()

class RecruiterList(ListAPIView):
    serializer_class = RecruiterSerializer
    queryset = Recruiter.objects.all()

class RecruiterDetail(RetrieveAPIView):
    serializer_class = RecruiterSerializer
    queryset = Recruiter.objects.all()