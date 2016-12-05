from django.shortcuts import render, get_object_or_404
from .models import Category
from projects.models import Project


def categories_list(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories/list.html', context)


def single_category(request, slug=None):
    category = get_object_or_404(Category, slug=slug)
    projects = Project.objects.filter(category=category)
    context = {
        'category': category,
        'projects': projects,
    }
    return render(request, 'categories/single.html', context)
