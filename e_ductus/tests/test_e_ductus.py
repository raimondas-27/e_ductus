from unittest import TestCase

from django.http import request
from e_ductus.models import Subject, Course
import pytest
from django.urls import resolve, reverse

from e_ductus.views import HomeView

from e_ductus.views import BaseView


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
        self.assertEqual(resolver.func.view_class, BaseView)


def test_admin(client):
    assert client.get('/').status_code == 200


@pytest.mark.django_db
def test_models():
    subject = Subject.objects.create(title="django1", slug="django")
    assert subject.title == "django1"
    assert subject.slug == "django"
