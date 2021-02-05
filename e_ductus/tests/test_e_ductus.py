from e_ductus.models import Subject, Course
import pytest


def test_admin(client):
    assert client.get('admin/').status_code == 200


@pytest.mark.django_db
def test_models():
    subject = Subject.objects.create(title="django1", slug="django")
    assert subject.title == "django1"
    assert subject.slug == "django"

#
# class OwnerMixinTest(SimpleTestCase):
#     class MyView(OwnerMixin, TemplateView):
#         pass
#
#     def test_owner_mixin(self):
#         my_view = self.MyView()
#         context = my_view.get_context_data()
#         self.assertTrue(context)
#
#
# class OwnerCourseEditMixinTest(unittest.TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_details(self):
#         response = self.client.get('/mine/')
#         self.assertEqual(response.status_code, 200)
#         # self.assertEqual(len(response.content['courses']),1)
