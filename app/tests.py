from django.test import TestCase, Client
from app.models import News
from datetime import date 
from django.http import HttpRequest,HttpResponse
from .views import main_page
from django.urls import reverse


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

    def test_views(self):
        client = Client()
        request = HttpRequest()
        response: HttpResponse = main_page(request)  
        response = client.get(reverse('index'))  


        self.assertTemplateUsed(response, 'index.html')

    

    



    