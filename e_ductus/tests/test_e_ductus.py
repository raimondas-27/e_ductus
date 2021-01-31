from unittest import TestCase

# from django.test import TestCase
from django.contrib.auth.models import User
from django.http import request
from django.test import Client, SimpleTestCase
from django.views.generic import TemplateView

from e_ductus.models import Subject, Course
import pytest
from django.urls import resolve, reverse
from e_ductus.views import HomeView
from e_ductus.views import BaseView
from e_ductus.views import OwnerMixin
from e_ductus.views import CourseDeleteView
from e_ductus.views import CourseUpdateView
from e_ductus.views import CourseCreateView
from e_ductus.views import ManageCourseListView




class HomeViewTest(TestCase):
    def test_resolve_to_home_page_view(self):
        resolver = resolve('/home/')
        self.assertEqual(resolver.func.view_class, HomeView)


class BaseViewTest(TestCase):
    def test_resolve_to_base_page_view(self):
        resolver = resolve('/')
        self.assertEqual(resolver.func.view_class, BaseView)


class CourseDeleteViewTest(TestCase):
    def test_resolve_to_course_delete_page_view(self):
        resolver = resolve('/<pk>/delete/')
        self.assertEqual(resolver.func.view_class,CourseDeleteView)


class CourseUpdateViewTest(TestCase):
    def test_resolve_to_course_update_page_view(self):
        resolver = resolve('/<pk>/edit/')
        self.assertEqual(resolver.func.view_class,CourseUpdateView)


class CourseCreateViewTest(TestCase):
    def test_resolve_to_course_create_page_view(self):
        resolver = resolve('/create/')
        self.assertEqual(resolver.func.view_class,CourseCreateView)


class ManageCourseListViewTest(TestCase):
    def test_resolve_to_manage_course_list_page_view(self):
        resolver = resolve('/mine/')
        self.assertEqual(resolver.func.view_class,ManageCourseListView)


class OwnerCourseEditMixinViewTest(TestCase):
    def test_resolve_to_owner_course_edit_mixin_page_view(self):
        resolver = resolve('/mine/')
        self.assertEqual(resolver.func.view_class,ManageCourseListView)


def test_admin(client):
    assert client.get('/').status_code == 200


@pytest.mark.django_db
def test_models():
    subject = Subject.objects.create(title="django1", slug="django")
    assert subject.title == "django1"
    assert subject.slug == "django"


class OwnerMixinTest(SimpleTestCase):
    
    class MyView(OwnerMixin, TemplateView):
        pass
    
    def test_owner_mixin(self):
        my_view = self.MyView()
        context = my_view.get_context_data()
        self.assertTrue(context)
        
