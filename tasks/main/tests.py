from django.test import TestCase


import os
import django
from django.test import TestCase
from django.core.asgi import get_asgi_application
from django.contrib.auth.models import User
from django.urls import path
from .models import Advert

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tasks.settings")
django_asgi_app = get_asgi_application()
django.setup()


class AdvertTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='tester2', password='12345')
        Advert.objects.create(title='Объявление 1', content='Тестовый комментарий 1')
        Advert.objects.create(title='Объявление 2', content='Тестовый комментарий 2', author=User.objects.get(id=1))


    def test_verbose_names(self):  #verbose_name проверка
        adv = Advert.objects.get(id=1)
        title = adv._meta.get_field('title').verbose_name
        content = adv._meta.get_field('content').verbose_name
        author = adv._meta.get_field('author').verbose_name
        self.assertEqual(title, 'Заголовок')
        self.assertEqual(content, 'Содержание')
        self.assertEqual(author, 'Автор')

    def test_str(self):
        adv = Advert.objects.get(id=1)
        self.assertEqual(adv.__str__(), 'Объявление 1')

    def test_max_length(self):
        adv = Advert.objects.get(id=1)
        max_length_title = adv._meta.get_field('title').max_length
        self.assertEqual(max_length_title, 70)

    def test_standard_author_value(self):
        adv = Advert.objects.get(id=1)
        self.assertIsNone(adv.author)

    def test_datetime_creates(self):
        adv = Advert.objects.get(id=1)p
        self.assertTrue(adv.create_date)

