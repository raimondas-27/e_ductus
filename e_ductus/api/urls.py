from django.urls import path
from .views import Subjectview
from .views import CourseView


urlpatterns = [
    path('home/', Subjectview.as_view()),
    path('about/',CourseView.as_view()),
]