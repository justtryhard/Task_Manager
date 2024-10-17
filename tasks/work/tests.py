import os
import django
from django.test import TestCase
from django.core.asgi import get_asgi_application
from django.contrib.auth.models import User
from .models import WorkTask, Comments

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tasks.settings")
django_asgi_app = get_asgi_application()
django.setup()


class WorkTaskTestCase(TestCase):


    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='tester2', password='12345')
        WorkTask.objects.create(title='address1', description='Тестовое описание 1')
        WorkTask.objects.create(title='address2', description='Тестовое описание 2', author=User.objects.get(id=1),
                                executor=User.objects.get(id=1))
        Comments.objects.create(worktask=WorkTask.objects.get(id=1), text='Тестовое описание 2')


    def test_verbose_names(self):  #verbose_name проверка
        task = WorkTask.objects.get(id=1)
        type = task._meta.get_field('type').verbose_name
        address = task._meta.get_field('title').verbose_name
        self.assertEqual(type, 'Тип')
        self.assertEqual(address, 'Адрес')

    def test_str(self):
        task = WorkTask.objects.get(id=1)
        self.assertEqual(task.__str__(), 'address1')

    def test_max_length(self):
        task = WorkTask.objects.get(id=1)
        max_length_title = task._meta.get_field('title').max_length
        max_length_type = task._meta.get_field('type').max_length
        self.assertEqual(max_length_title, 50)
        self.assertEqual(max_length_type, 15)

    def test_standard_values(self):
        task = WorkTask.objects.get(id=1)
        comment = Comments.objects.get(id=1)
        self.assertIsNone(task.author)
        self.assertIsNone(task.executor)
        self.assertIsNone(comment.author)
        self.assertFalse(comment.status)
        self.assertEqual(task.type, "Аварийный выезд")
        self.assertEqual(task.status, "Открыта")


    def test_users(self):
        task = WorkTask.objects.get(id=2)
        user = User.objects.get(id=1)
        self.assertEqual(task.executor, user)
        self.assertEqual(task.author, user)

    def test_links(self):
        task = WorkTask.objects.get(id=1)
        comment = Comments.objects.get(id=1)
        self.assertEqual(comment.worktask, task)

    def test_datetime_creates(self):
        task = WorkTask.objects.get(id=1)
        comment = Comments.objects.get(id=1)
        self.assertTrue(task.create_date)
        self.assertTrue(comment.create_date)

