from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.BaseView.as_view(template_name='base.html'), name='base'),

    path('home/', views.HomeView.as_view(template_name='home.html'), name='home'),

    path('admin/', admin.site.urls, name='admin'),

    path('accounts/login/', auth_views.LoginView.as_view(),
         name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(),
         name='logout'),

    path('mine/',
         views.ManageCourseListView.as_view(),
         name='manage_course_list'),
    path('create/',
         views.CourseCreateView.as_view(),
         name='course_create'),
    path('<pk>/edit/',
         views.CourseUpdateView.as_view(),
         name='course_edit'),
    path('<pk>/delete/',
         views.CourseDeleteView.as_view(),
         name='course_delete'),
]
