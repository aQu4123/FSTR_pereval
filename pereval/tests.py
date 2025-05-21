from django.test import TestCase

from django.test import TestCase
from .models import Added, User


# class PassModelTest(TestCase):
#
#     def setUp(self):
#         # Создаем пользователя для тестов
#         self.user = User.objects.create(
#             email="testuser@example.com",
#             phone="1234567890",
#             fam="Иванов",
#             name="Иван",
#             otc="Иванович"
#         )
#
#     def test_pass_creation(self):
#         # Создаем запись Pass
#         pass_instance = Added.objects.create(
#             beautyTitle="Beautiful Pass",
#             title="Test Pass",
#             latitude=45.0,
#             longitude=90.0,
#             height=3000,
#             user=self.user
#         )
#         self.assertEqual(pass_instance.title, "Test Pass")
#         self.assertEqual(pass_instance.user.email, "testuser@example.com")
#
#     def test_default_status(self):
#         # Проверяем, что статус по умолчанию - 'new'
#         pass_instance = Added.objects.create(
#             beautyTitle="Another Pass",
#             title="Another Test Pass",
#             latitude=50.0,
#             longitude=100.0,
#             height=3500,
#             user=self.user
#         )
#         self.assertEqual(pass_instance.status, "new")