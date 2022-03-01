from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('Main page')


    # Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse('Group posts with slug {}'.format(slug))



# Create your views here.
