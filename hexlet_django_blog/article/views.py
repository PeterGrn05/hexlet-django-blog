from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'app_name': 'hexlet_django_blog.article',
            'page_title': 'Главная страница блога',
            'welcome_message': 'Добро пожаловать в блог!',
        }
        return render(
            request,
            'articles/index.html',
            context
        )
# Create your views here.
