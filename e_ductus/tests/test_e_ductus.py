from unittest import TestCase
import pytest
from e_ductus.models import Subject
from django.urls import resolve
from e_ductus.views import HomeView
from e_ductus.views import BaseView
from e_ductus.views import CourseDeleteView
from e_ductus.views import CourseUpdateView
from e_ductus.views import CourseCreateView
from e_ductus.views import ManageCourseListView


# def test_base(client):
#     assert client.get('').status_code == 200


# def test_home(client):
#     assert client.get('/home/').status_code == 200


class HomeViewTest(TestCase):
    def test_resolve_to_home_page_view(self):
        resolver = resolve('/home/')
        self.assertEqual(resolver.func.view_class, HomeView)


class BaseViewTest(TestCase):
    def test_resolve_to_base_page_view(self):
        resolver = resolve('/')
        self.assertEqual(resolver.func.view_class,BaseView)


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
