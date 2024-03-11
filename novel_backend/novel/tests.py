from django.test import TestCase

# ref https://docs.djangoproject.com/zh-hans/4.2/topics/testing/overview/

from rest_framework.test import APIRequestFactory
from .views import NovelViewSet
from .models import Novel


class ApiTestCase(TestCase):
    def setUp(self):
        Novel.objects.create(name="a book", desc="desc", max_chapter=3)

    def test_get_and_post(self):
        # current only test status code.
        factory = APIRequestFactory()
        request = factory.get('/novel/')
        response = NovelViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
        # handle POST
        request = factory.post('/novel/', {'name': 'Another book', 'desc': 'Desc', 'max_chapter': 3})
        response = NovelViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, 201)
