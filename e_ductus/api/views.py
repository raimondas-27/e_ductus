from django.shortcuts import render
from rest_framework import generics
from .models import Course
from .models import Subject
from .serializers import SubjectSerializer, CourseSerializer

# Create your views here.

class Subjectview(generics.ListAPIView):
    queryset = Subject.objects.all
    serializer_class = SubjectSerializer



class CourseView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
