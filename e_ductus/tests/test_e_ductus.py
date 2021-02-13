from django import urls
import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse


@pytest.mark.parametrize("param", [
    ("course_list"),

])
def test_render_views(admin_client, param):
    temp_url = urls.reverse(param)
    response = admin_client.get(temp_url)
    assert response.status_code == 200


@pytest.mark.parametrize("param1", [

    ("manage_course_list"),
    ("course_create"),
    # ("course_edit"),
    # ("course_delete"),

])
def test_superusers_functionality_view(admin_client, param1):
    temp_url = urls.reverse(param1)
    response = admin_client.get(temp_url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_functionality(admin_client):
    url = reverse("module_order")
    response = admin_client.get(url)
    assert response.status_code == 405


@pytest.mark.django_db
def test_user_login(client, create_test_user, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse("login")
    resp = client.post(login_url, data=user_data)
    assert resp.status_code == 302


@pytest.mark.django_db
def test_user_logout(client, authenticated_user):
    logout_url = urls.reverse("logout")
    print(logout_url)
    resp = client.get(logout_url)
    assert resp.status_code == 302


# @pytest.mark.django_db
# def test_student_registration(client, user_data):
#     user_model = get_user_model()
#     assert user_model.objects.count() == 0
#     signup_url = urls.reverse("student_registration")
#     resp = client.post(signup_url, user_data)
#     assert user_model.objects.count() == 1
#     assert resp.status_code == 302



