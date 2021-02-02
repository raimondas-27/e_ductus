from django import urls
import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse


@pytest.mark.parametrize("param", [
    ("home"),
    ("base"),
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    resp = client.get(temp_url)
    assert resp.status_code == 200


@pytest.mark.django_db
def test_user_login(client, create_test_user, user_data):
    user_model = get_user_model()
    assert user_model.objects.count() == 1
    login_url = urls.reverse("login")
    resp = client.post(login_url, data=user_data)
    assert resp.status_code == 302


# @pytest.mark.django_db
# def test_user_logout(client, authenticated_user):
#     logout_url = urls.reverse("logout")
#     resp = client.get(logout_url)
#     assert resp.status_code == 302
#     assert resp.url == urls.reverse('home')

# @pytest.mark.django_db
# def test_superuser_view(admin_client):
#     url = reverse('admin')
#     response = admin_client.get(url)
#     assert response.status_code == 200
