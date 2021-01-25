from e_ductus.models import Subject, Course
import pytest
from django.test import TestCase

# from e_ductus.models import Course


def test_base(client):
    assert client.get('/').status_code == 200


def test_home(client):
    assert client.get('/home/').status_code == 200


def test_admin(client):
    assert client.get('/').status_code == 200


# class TestModels(TestCase):
#     def test_models(self):
#         title = Subject.objects.create(title="django_testing")
#         slug = Subject.objects.create(slug="this my slug")
#         self.assertEqual(str(title), "django_testing")
#         self.assertEqual(str(slug), "this my slug")

@pytest.mark.django_db
def test_models():
    subject = Subject.objects.create(title="django1", slug="django")
    # course = Course.objects.create(title="title")
    # assert course.title == "title"
    assert subject.title == "django1"
    assert subject.slug == "django"


# @pytest.mark.django_db
# def test_models_course():
#     course = Course.objects.create(title="title")
#     assert course.title == "title"
