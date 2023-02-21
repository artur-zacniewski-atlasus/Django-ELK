import logging

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets

from blog.models import Category, Article
from blog.serializers import CategorySerializer, ArticleSerializer, UserSerializer

logger = logging.getLogger(__name__)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


def error_log_view(request):
    logger.error(f"The {request.get_host()} host is not secure!")
    return HttpResponse("Error log")


def info_log_view(request):
    logger.info("This is an info message")
    return HttpResponse("Info log")


def debug_log_view(request):
    logger.debug("This is a debug message", extra={'extraParam': 'OWI'})
    return HttpResponse("Debug log")

