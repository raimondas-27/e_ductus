from e_ductus.models import Subject, Course
import pytest


def test_base(client):
    assert client.get('/').status_code == 200


def test_home(client):
    assert client.get('/home/').status_code == 200


def test_admin(client):
    assert client.get('/').status_code == 200


@pytest.mark.django_db
def test_models():
    subject = Subject.objects.create(title="django1", slug="django")
    assert subject.title == "django1"
    assert subject.slug == "django"
