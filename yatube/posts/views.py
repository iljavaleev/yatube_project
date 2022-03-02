from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):    
    template_name = "posts/index.html"
    text = "Это главная страница проекта Yatube"
    context = {
        'text': text
    }
    return render(request, template_name, context)


    # Страница со списком мороженого
def group_posts(request, slug):
    template_name = "posts/group_list.html"
    text = "Здесь будет информация о группах проекта Yatube"
    context = {
        'text': text
    }
    return render(request, template_name, context)




