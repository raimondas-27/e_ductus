from e_ductus.models import Subject, Course
import pytest


@pytest.mark.django_db
def test_models():
    subject = Subject.objects.create(title="django1", slug="django")
    assert subject.title == "django1"
    assert subject.slug == "django"


def test_student_register(client):
    assert client.get('/register/').status_code == 200


def test_admin(client):
    assert client.get('').status_code == 200


# def test_enrollment(client):
#     assert client.get('/enroll-course/').status_code == 200
# #
#
# def test_student_register(client):
#     assert client.get('/register/').status_code == 200
