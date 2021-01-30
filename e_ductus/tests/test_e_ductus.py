from e_ductus.api.models import Subject, Course
import pytest
from django.urls import resolve
from e_ductus.api.views import BaseView
from e_ductus.api.views import OwnerMixin
from unittest import TestCase
import django.test
from django.test import Client
from django.contrib.auth.models import User
from e_ductus.api.views import CourseDeleteView



class CourseDeleteViewTest(TestCase):
    def test_resolve_to_delete_page_view(self):
        resolver = resolve("/courses/manage/course/delete.html/")
        self.assertEqual(resolver.func.view_class, CourseDeleteView)


class BaseViewTest(TestCase):
    def test_resolve_to_home_page_view(self):
        resolver = resolve("/home/")
        self.assertEqual(resolver.func.view_class, BaseView)


class OwnerMixingTest(TestCase):
    def setUp(self):
        self.user = User(username='jimish')
        password = 'password'
        self.user.set_password(password)
        self.user.save()

        self.client = Client()
        self.client.login(username=self.user.username, password=password)



    def test_resolve_getting_queryset(self):





def test_admin(client):
    assert client.get('/').status_code == 200


@pytest.mark.django_db
def test_models():
    subject = Subject.objects.create(title="django1", slug="django")
    assert subject.title == "django1"
    assert subject.slug == "django"