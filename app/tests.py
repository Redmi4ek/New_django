from django.test import TestCase
from app.models import News
from datetime import date 

class newsData(TestCase):
    def setUp(self):
        self.news_instance = News.objects.create(
            public='Some public content',
            date=date(2022, 1, 1)
        )

    def test_public_field_presence(self):
        queried_news = News.objects.filter(public='Some public content').first()
        self.assertIsNotNone(queried_news)
        self.assertEqual(queried_news.public, 'Some public content')

    def test_date_field_type(self):
        self.assertIsInstance(self.news_instance.date, date)

    def test_news_instance_creation(self):
        # Проверяем, что объект News был создан успешно
        self.assertEqual(self.news_instance.public, 'Some public content')
        self.assertEqual(self.news_instance.date, date(2022, 1, 1))
        self.assertIsNotNone(self.news_instance.id)

    