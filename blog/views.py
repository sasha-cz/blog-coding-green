from django.shortcuts import render
from .models import Blogpost
from rest_framework import views, status
from rest_framework.response import Response  
from .serializers import BlogpostSerializer


# Create views for two endpoints: Get a list of all articles + get individual article)
class ArticleList(views.APIView):
    def get(self, request): 
        articles = Blogpost.objects.filter(approval_status='approved').order_by("-date")[:20]
        serializer = BlogpostSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class Article(views.APIView):
    def get(self, request, slug):
        try:    
            article = Blogpost.objects.get(slug=slug)
            serializer = BlogpostSerializer(article)
            return Response(serializer.data)
        except Blogpost.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)
            
