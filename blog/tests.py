from django.test import TestCase
from .models import Blogpost
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status


class ArticleDetailTestCase(APITestCase):

    """
    Test suite for article_detail
    """
    def setUp(self):
        self.client = APIClient() # APIClient constructs a client
        self.data = {
            "title": "What is Green Coding?",
            "content": "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. For me, the most fascinating interface is Twitter. I have odd cosmic thoughts every day and I realized I could hold them to myself or share them with people who might be interested. For me, the most fascinating interface is Twitter. I have odd cosmic thoughts every day and I realized I could hold them to myself or share them with people who might be interested. I have odd cosmic thoughts every day For me, the most fascinating interface is Twitter. I have odd cosmic thoughts every day and I realized I could hold them to myself or share them with people who might be interested. Venus has a runaway greenhouse effect. I kind of want to know what happened there because we're twirling knobs here on Earth without knowing the consequences of it. Mars once had running water. It's bone dry today. Something bad happened there as well.",
            "author": "Alexandra Pietroch", 
            "date": "2023-10-24T08:35:44.175853Z",
        }
        self.url = "/basic/"



   